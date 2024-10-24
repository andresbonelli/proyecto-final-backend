from datetime import datetime
from fastapi import APIRouter, BackgroundTasks, HTTPException, status, Response
from fastapi.responses import JSONResponse
from pydantic import EmailStr
from pydantic_mongo import PydanticObjectId
from passlib.exc import UnknownHashError

from ..models import (
    UserRegisterData,
    UserLoginData,
    UserUpdateData,
    PrivateUserFromDB,
    UserVerifyRequest,
    UserResetPasswordRequest
)
from ..services import (
    UsersServiceDependency,
    AuthServiceDependency,
    SecurityDependency,
    RefreshCredentials,
    send_account_verification_email,
    send_reset_password_email
)

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user: UserRegisterData,
    users: UsersServiceDependency,
    auth: AuthServiceDependency,
    background_tasks: BackgroundTasks,
):
    user.role = "customer"
    hash_password = auth.get_password_hash(user.password)
    result = users.create_one(user, hash_password)
   
    if new_user := users.get_one(id=result.inserted_id, with_password=True):
        print(f"user created with id: {new_user.id}")
        await send_account_verification_email(user=new_user, background_tasks=background_tasks)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Un error inesperado ha ocurrido al crear tu cuenta. Lo sentimos."
        )
    return {"message": "¡Cuenta creada! Revisá tu Email (también Spam). Un link de activación estará llegando en unos minutos.",
            "inserted_id": f"{result.inserted_id}"}

@auth_router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_user_account(
    verify_request: UserVerifyRequest,
    users: UsersServiceDependency,
    auth: AuthServiceDependency,
):
    user_from_db = users.get_one(email=verify_request.email, with_password=True)
    if not user_from_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    if user_from_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="¡La cuenta ya está verificada!"
        )
    context_time: datetime = user_from_db.modified_at or user_from_db.created_at 
    context_string = f"{user_from_db.hash_password}{context_time.strftime('%d/%m/%Y,%H:%M:%S')}-verify" 
    try:
        if auth.verify_password(context_string, verify_request.token):
            if users.update_one(
                user_from_db.id,
                UserUpdateData(is_active=True)
                ):
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={"message": "¡Cuenta verificada! Ya puedes iniciar sesión."}
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Link expirado o inválido"
            )
    except UnknownHashError:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token inválido"
            )
        
@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login_with_cookie(
    user: UserLoginData,
    response: Response,
    users: UsersServiceDependency,
    auth: AuthServiceDependency,
):
    """
    Login with username or email
    """
    user_from_db = users.get_one(
        username=user.input if "@" not in user.input else None,
        email=user.input if "@" in user.input else None,
        with_password=True
    )
    if not user_from_db or not user_from_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no existe o fue desactivado"
            )
    return auth.login_and_set_access_token(
        password=user.password,
        user_from_db=user_from_db.model_dump(),
        response=response
    )

@auth_router.get("/authenticated_user", status_code=status.HTTP_200_OK)
async def read_current_user(security: SecurityDependency):
    return dict(
        id=str(security.auth_user_id),
        username=security.auth_user_name,
        role=security.auth_user_role,
        created_at=security.auth_user_created_at,
        modified_at=security.auth_user_modified_at,
        is_active=security.auth_user_is_active,
    )

@auth_router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_credentials(
    response: Response,
    auth: AuthServiceDependency,
    users: UsersServiceDependency,
    refresh: RefreshCredentials
    ):
    user_id = PydanticObjectId(refresh["id"])
    user_from_db = users.get_one(id=user_id)
    if not user_from_db or not user_from_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no existe o fue desactivado"
            )
    return auth.refresh_access_token(response, refresh)

@auth_router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def user_forgot_password(
    email: EmailStr,
    users: UsersServiceDependency,
    background_tasks: BackgroundTasks
):
    user_from_db: PrivateUserFromDB = users.get_one(email=email, with_password=True)
    if not user_from_db or not user_from_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no existe o fue desactivado"
            )
    await send_reset_password_email(user_from_db, background_tasks=background_tasks)
    return JSONResponse({"message": f"revisá tu Email {email} (también Spam). Un link de restablecimiento estará llegando en unos minutos."})

@auth_router.put("/reset-password", status_code=status.HTTP_200_OK)
async def user_reset_password(
    verify_request: UserResetPasswordRequest,
    auth: AuthServiceDependency,
    users: UsersServiceDependency
):
    user_from_db: PrivateUserFromDB = users.get_one(email=verify_request.email, with_password=True)
    if not user_from_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tu cuenta fue suspendida. Por favor contacta a soporte técnico."
        )
        
    context_string = f"{user_from_db.hash_password}{user_from_db.modified_at.strftime('%d/%m/%Y,%H:%M:%S')}-reset-password" 
    try:
        if not auth.verify_password(context_string, verify_request.token):
             raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Link expirado o inválido"
            )
        users.update_password(user_from_db.id, auth.get_password_hash(verify_request.new_password))
        return JSONResponse({"message": "¡Nueva contraseña generada!"})
    except UnknownHashError:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token inválido"
            )
