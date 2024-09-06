__all__ = ["CountryCode"]

from enum import Enum

class CountryCode(list[str, str], Enum):
    AFGHANISTAN = ["AFG", "004"]
    ALBANIA = ["ALB", "008"]
    ALGERIA = ["DZA", "012"]
    AMERICAN_SAMOA = ["ASM", "016"]
    ANDORRA = ["AND", "020"]
    ANGOLA = ["AGO", "024"]
    ANGUILLA = ["AIA", "660"]
    ANTIGUA_AND_BARBUDA = ["ATG", "028"]
    ARGENTINA = ["ARG", "032"]
    ARMENIA = ["ARM", "051"]
    ARUBA = ["ABW", "533"]
    AUSTRALIA = ["AUS", "036"]
    AUSTRIA = ["AUT", "040"]
    AZERBAIJAN = ["AZE", "031"]
    BAHAMAS = ["BHS", "044"]
    BAHRAIN = ["BHR", "048"]
    BANGLADESH = ["BGD", "050"]
    BARBADOS = ["BRB", "052"]
    BELARUS = ["BLR", "112"]
    BELGIUM = ["BEL", "056"]
    BELGIUM_LUXEMBOURG = ["BLX", "058"]
    BELIZE = ["BLZ", "084"]
    BENIN = ["BEN", "204"]
    BERMUDA = ["BMU", "060"]
    BHUTAN = ["BTN", "064"]
    BOLIVIA = ["BOL", "068"]
    BOSNIA_AND_HERZEGOVINA = ["BIH", "070"]
    BOTSWANA = ["BWA", "072"]
    BRITISH_ANTARCTIC_TERRITORY = ["BAT", "080"]
    BRAZIL = ["BRA", "076"]
    BRITISH_INDIAN_OCEAN_TERRITORY = ["IOT", "086"]
    BRITISH_VIRGIN_ISLANDS = ["VGB", "092"]
    BRUNEI = ["BRN", "096"]
    BULGARIA = ["BGR", "100"]
    BURKINA_FASO = ["BFA", "854"]
    BURUNDI = ["BDI", "108"]
    CAMBODIA = ["KHM", "116"]
    CAMEROON = ["CMR", "120"]
    CANADA = ["CAN", "124"]
    CAPE_VERDE = ["CPV", "132"]
    CAYMAN_ISLANDS = ["CYM", "136"]
    CENTRAL_AFRICAN_REPUBLIC = ["CAF", "140"]
    CHAD = ["TCD", "148"]
    CHILE = ["CHL", "152"]
    CHINA = ["CHN", "156"]
    CHRISTMAS_ISLAND = ["CXR", "162"]
    COCOS_KEELING_ISLANDS = ["CCK", "166"]
    COLOMBIA = ["COL", "170"]
    COMOROS = ["COM", "174"]
    CONGO_DEM_REP = ["ZAR", "180"]
    CONGO_REP = ["COG", "178"]
    COOK_ISLANDS = ["COK", "184"]
    COSTA_RICA = ["CRI", "188"]
    COTE_D_IVOIRE = ["CIV", "384"]
    CROATIA = ["HRV", "191"]
    CUBA = ["CUB", "192"]
    CYPRUS = ["CYP", "196"]
    CZECH_REPUBLIC = ["CZE", "203"]
    CZECHOSLOVAKIA = ["CSK", "200"]
    DENMARK = ["DNK", "208"]
    DJIBOUTI = ["DJI", "262"]
    DOMINICA = ["DMA", "212"]
    DOMINICAN_REPUBLIC = ["DOM", "214"]
    EAST_TIMOR = ["TMP", "626"]
    ECUADOR = ["ECU", "218"]
    EGYPT_ARAB_REP = ["EGY", "818"]
    EL_SALVADOR = ["SLV", "222"]
    EQUATORIAL_GUINEA = ["GNQ", "226"]
    ERITREA = ["ERI", "232"]
    ESTONIA = ["EST", "233"]
    ETHIOPIA_EXCLUDES_ERITREA = ["ETH", "231"]
    ETHIOPIA_INCLUDES_ERITREA = ["ETF", "230"]
    EUROPEAN_UNION = ["EUN", "918"]
    FAEROE_ISLANDS = ["FRO", "234"]
    FALKLAND_ISLAND = ["FLK", "238"]
    FIJI = ["FJI", "242"]
    FINLAND = ["FIN", "246"]
    FM_PANAMA_CZ = ["PCZ", "592"]
    FM_ROD_NIAS = ["ZW1", "717"]
    FM_TANGANYIK = ["TAN", "835"]
    FM_VIETNAM_DR = ["VDR", "868"]
    FM_VIETNAM_RP = ["SVR", "866"]
    FM_ZANZ_PEMBA = ["ZPM", "836"]
    FR_SO_ANT_TR = ["ATF", "260"]
    FRANCE = ["FRA", "250"]
    FREE_ZONES = ["FRE", "838"]
    FRENCH_GUIANA = ["GUF", "254"]
    FRENCH_POLYNESIA = ["PYF", "258"]
    GABON = ["GAB", "266"]
    GAMBIA_THE = ["GMB", "270"]
    GAZA_STRIP = ["GAZ", "274"]
    GEORGIA = ["GEO", "268"]
    GERMAN_DEMO_CRATIC_REPUBLIC = ["DDR", "278"]
    GERMANY = ["DEU", "276"]
    GHANA = ["GHA", "288"]
    GIBRALTAR = ["GIB", "292"]
    GREECE = ["GRC", "300"]
    GREENLAND = ["GRL", "304"]
    GRENADA = ["GRD", "308"]
    GUadeloupe = ["GLP", "312"]
    GUAM = ["GUM", "316"]
    GUATEMALA = ["GTM", "320"]
    GUINEA = ["GIN", "324"]
    GUINEA_BISSAU = ["GNB", "624"]
    GUYANA = ["GUY", "328"]
    HAITI = ["HTI", "332"]
    HOLY_SEE = ["VAT", "336"]
    HONDURAS = ["HND", "340"]
    HONG_KONG_CHINA = ["HKG", "344"]
    HUNGARY = ["HUN", "348"]
    ICELAND = ["ISL", "352"]
    INDIA = ["IND", "356"]
    INDONESIA = ["IDN", "360"]
    IRAN_ISLAMIC_REP = ["IRN", "364"]
    IRAQ = ["IRQ", "368"]
    IRELAND = ["IRL", "372"]
    ISRAEL = ["ISR", "376"]
    ITALY = ["ITA", "380"]
    JAMAICA = ["JAM", "388"]
    JAPAN = ["JPN", "392"]
    JOHNSTON_ISLAND = ["JTN", "396"]
    JORDAN = ["JOR", "400"]
    KAZAKHSTAN = ["KAZ", "398"]
    KENYA = ["KEN", "404"]
    KIRIBATI = ["KIR", "296"]
    KOREA_DEM_REP = ["PRK", "408"]
    KOREA_REP = ["KOR", "410"]
    KUWAIT = ["KWT", "414"]
    KYRGYZ_REPUBLIC = ["KGZ", "417"]
    LAO_PDR = ["LAO", "418"]
    LATVIA = ["LVA", "428"]
    LEBANON = ["LBN", "422"]
    LESOTHO = ["LSO", "426"]
    LIBERIA = ["LBR", "430"]
    LIBYA = ["LBY", "434"]
    LIECHTENSTEIN = ["LIE", "438"]
    LITHUANIA = ["LTU", "440"]
    LUXEMBOURG = ["LUX", "442"]
    MACAO = ["MAC", "446"]
    MACEDONIA_FYRO = ["MKD", "807"]
    MADAGASCAR = ["MDG", "450"]
    MALAWI = ["MWI", "454"]
    MALAYSIA = ["MYS", "458"]
    MALDIVES = ["MDV", "462"]
    MALI = ["MLI", "466"]
    MALTA = ["MLT", "470"]
    MARSHALL_ISLANDS = ["MHL", "584"]
    MARTINIQUE = ["MTQ", "474"]
    MAURITANIA = ["MRT", "478"]
    MAURITIUS = ["MUS", "480"]
    MEXICO = ["MEX", "484"]
    MICRONESIA_FED_STATES = ["FSM", "583"]
    MIDWAY_ISLANDS = ["MID", "488"]
    MOLDOVA = ["MDA", "498"]
    MONACO = ["MCO", "492"]
    MONGOLIA = ["MNG", "496"]
    MONTSERRAT = ["MSR", "500"]
    MOROCCO = ["MAR", "504"]
    MOZAMBIQUE = ["MOZ", "508"]
    MYANMAR = ["MMR", "104"]
    NAMIBIA = ["NAM", "516"]
    NAURU = ["NRU", "520"]
    NEPAL = ["NPL", "524"]
    NETHERLANDS = ["NLD", "528"]
    NETHERLANDS_ANTILLES = ["ANT", "530"]
    NEUTRAL_ZONE = ["NZE", "536"]
    NEW_CALEDONIA = ["NCL", "540"]
    NEW_ZEALAND = ["NZL", "554"]
    NICARAGUA = ["NIC", "558"]
    NIGER = ["NER", "562"]
    NIGERIA = ["NGA", "566"]
    NIUE = ["NIU", "570"]
    NORFOLK_ISLAND = ["NFK", "574"]
    NORTHERN_MARIANA_ISLANDS = ["MNP", "580"]
    NORWAY = ["NOR", "578"]
    OMAN = ["OMN", "512"]
    PACIFIC_ISLANDS = ["PCE", "582"]
    PAKISTAN = ["PAK", "586"]
    PALAU = ["PLW", "585"]
    PANAMA = ["PAN", "591"]
    PAPUA_NEW_GUINEA = ["PNG", "598"]
    PARAGUAY = ["PRY", "600"]
    PEN_MALAYSIA = ["PMY", "459"]
    PERU = ["PER", "604"]
    PHILIPPINES = ["PHL", "608"]
    PITCAIRN = ["PCN", "612"]
    POLAND = ["POL", "616"]
    PORTUGAL = ["PRT", "620"]
    PUERTO_RICO = ["PRI", "630"]
    QATAR = ["QAT", "634"]
    ROMANIA = ["ROU", "642"]
    RUSSIAN_FEDERATION = ["RUS", "643"]
    RWANDA = ["RWA", "646"]
    SAINT_KITTS_AND_NEVIS = ["KNA", "659"]
    SAINT_LUCIA = ["LCA", "670"]
    SAINT_PIERRE_AND_MIQUELON = ["SPM", "674"]
    SAINT_VINCENT_AND_THE_GRENADINES = ["VCT", "670"]
    SAMOA = ["WSM", "882"]
    SAN_MARINO = ["SMR", "674"]
    SAO_TOME_AND_PRINCIPYE = ["STP", "678"]
    SAUDI_ARABIA = ["SAU", "682"]
    SENEGAL = ["SEN", "686"]
    SERBIA = ["SRB", "688"]
    SEYCHELLES = ["SYC", "690"]
    SIERRA_LEONE = ["SLE", "694"]
    SINGAPORE = ["SGP", "702"]
    SINT_MAARTEN = ["SXM", "916"]
    SIRIA = ["SYR", "760"]
    SLOVENIA = ["SVN", "705"]
    SOLOMON_ISLANDS = ["SLB", "090"]
    SOMALIA = ["SOM", "706"]
    SOUTH_AFRICA = ["ZAF", "710"]
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = ["SGS", "729"]
    SOUTH_KOREA = ["KOR", "410"]
    SOUTH_SUDAN = ["SSD", "728"]
    SPAIN = ["ESP", "724"]
    SRI_LANKA = ["LKA", "144"]
    SUDAN = ["SDN", "736"]
    SURINAME = ["SUR", "740"]
    SWAZILAND = ["SWZ", "748"]
    SWEDEN = ["SWE", "752"]
    SWITZERLAND = ["CHE", "756"]
    SYRIA = ["SYR", "760"]
    TAIWAN = ["TWN", "158"]
    TAJIKISTAN = ["TJK", "762"]
    TANZANIA_UNITED_REPUBLIC = ["TZA", "834"]
    THAILAND = ["THA", "764"]
    TOGO = ["TGO", "768"]
    TOKELAU = ["TKL", "772"]
    TONGA = ["TON", "776"]
    TRINIDAD_AND_TOBAGO = ["TTO", "780"]
    TUNISIA = ["TUN", "788"]
    TURKEY = ["TUR", "796"]
    TURKMENISTAN = ["TKM", "795"]
    TUVALU = ["TUV", "798"]
    UGANDA = ["UGA", "800"]
    UKRAINE = ["UKR", "804"]
    UNITED_ARAB_EMIRATES = ["ARE", "784"]
    UNITED_KINGDOM = ["GBR", "826"]
    UNITED_STATES = ["USA", "840"]
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = ["UMI", "581"]
    URUGUAY = ["URY", "858"]
    UZBEKISTAN = ["UZB", "860"]
    VANUATU = ["VUT", "548"]
    VATICAN_CITY_STATE = ["VAT", "336"]
    VENEZUELA = ["VEN", "862"]
    VIETNAM = ["VNM", "704"]
    YEMEN = ["YEM", "887"]
    ZAMBIA = ["ZMB", "894"]
    ZIMBABWE = ["ZWE", "716"]
