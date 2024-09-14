__all__ = ["orders_router"]

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic_mongo import PydanticObjectId
from datetime import datetime

from ..__common_deps import QueryParamsDependency
from ..models import BaseOrder, OrderStatus, OrderUpdateData
from ..services import (
    OrdersServiceDependency,
    ProductsServiceDependency,
    SecurityDependency,
)

orders_router = APIRouter(prefix="/orders", tags=["Orders"])

@orders_router.get("/get_all")
async def get_all_orders(orders: OrdersServiceDependency, security: SecurityDependency, params: QueryParamsDependency):
    """
    Admins only!
    """
    security.is_admin_or_raise
    return orders.get_all(params)

@orders_router.get("/{id}")
async def get_order_by_id(id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency):
    """
    Staff members and admins only!
    """
    security.is_staff_or_raise
    return orders.get_one(id).model_dump()

@orders_router.get("/get_by_customer/{id}")
async def get_orders_by_customer_id(id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency):
    """
    Authenticated customer only!
    """
    security.check_user_permission(str(id))
    return orders.find_from_customer_id(id)
  
@orders_router.get("/get_by_product/{id}")
async def get_orders_by_product_id(id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency):
    """
    Staff members and admins only!
    """
    security.is_staff_or_raise
    return orders.find_from_product_id(id)

@orders_router.get("/get_by_staff/{id}")
async def get_orders_by_staff_id(id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency):
    """
    Authenticated staff member only!
    """
    security.check_user_permission(str(id))
    return orders.find_from_staff_id(id)

# Purchase order (multiple products). 
@orders_router.post("/")
async def create_order(
    order: BaseOrder,
    orders: OrdersServiceDependency,
    products: ProductsServiceDependency,
    security: SecurityDependency,
):
    """
    Customers only!
    """
    security.is_customer_or_raise
    
    #Prepare Order and store in database
    products.check_stock(order.products)
    new_order: dict = {
        "customer_id": PydanticObjectId(security.auth_user_id),
        "products": [
                {
                "product_id": PydanticObjectId(product.product_id),
                "quantity": product.quantity
                }
                for product in order.products
            ],
        "status": OrderStatus.pending,
        "created_at": datetime.now()
    }
    result = orders.create_one(new_order)
    if result.acknowledged:
        return {"result message": "Order succesfully created",
                "inserted_id": f"{result.inserted_id}"}
    else:
        return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"error": f"An unexpected error ocurred while creating order"},
            )

@orders_router.patch("/complete/{id}")
async def complete_order(
    id: PydanticObjectId,
    security: SecurityDependency,
    orders: OrdersServiceDependency,
    products: ProductsServiceDependency
):
    """
    Authenticated customer only!
    """
    existing_order = orders.get_one(id)
    security.check_user_permission(str(existing_order.customer_id))
    
    if existing_order.status == OrderStatus.pending:
        # Update product stock and sales count
        products.check_and_update_stock(existing_order.products)
        total_price = orders.calculate_total_price(id)
        result = orders.update_one(id, OrderUpdateData(
            status=OrderStatus.completed,
            total_price=total_price[0]
            ))
        return {"message": "Order succesfully fulfilled","Completed order": result}
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot complete order {id} with status {existing_order.status}"
        )
    
@orders_router.patch("/cancel/{id}")
async def cancel_order(id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency):
    """
    Authenticated customer only!
    """
    existing_order = orders.get_one(id)
    security.check_user_permission(str(existing_order.customer_id))
    
    if existing_order.status == OrderStatus.pending:
        result = orders.update_one(id, OrderUpdateData(status=OrderStatus.cancelled))
        return {"message": "Order cancelled!","Cancelled order": result}
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot cancel order {id} with status {existing_order.status}"
        )