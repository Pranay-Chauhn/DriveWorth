from enum import Enum
from pydantic import BaseModel


class FuelType(str, Enum):
    Gasoline = "Gasoline"
    Hybrid = "Hybrid"
    Unknown = "Unknown"
    Diesel = "Diesel"
    Electric = "Electric"
    Plug_In_Hybrid = "Plug-In Hybrid"
    E85_flex_Fuel = "E85 Flex Fuel"


class Accident(str, Enum):
    None_Reported = "None_reported"
    At_least_1_accident_or_damage_reported = "At least 1 accident or damage reported"


class CleanTitle(str, Enum):
    Yes = "Yes"
    No = "No"


class TransType(str, Enum):
    Automatic = "Automatic"
    Manual = "Manual"
    Other = "Other"


class CarFeatures(BaseModel):
    milage: float
    brand: str
    model: str
    model_year: int
    fuel_type : FuelType
    ext_col: str
    int_col: str
    accident : Accident
    clean_title : CleanTitle
    trans_type : TransType
    gear: int
    horsepower: int
    engine_size: int
    cylinders: int
