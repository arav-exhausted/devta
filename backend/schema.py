from pydantic import BaseModel, Field 
from typing import Literal,Optional,List


class DeliveyInput(BaseModel):
    age: int  = Field(..., ge = 18 , le=60)

    rating: float = Field(...,ge=1,le=5)

    distance: float = Field(...,ge=0,le=40)

    weather: Literal[
        'Sunny',
        "Cloudy",
        "Windy",
        "Stormy",
        "Fog",
        "Sandstorms"

    ]

    traffic: Literal[
        "Low",
        "Medium",
        "High",
        "Jam"
    ]

    vehicle_condition: int = Field(...,ge=0,le=3)

    order_type: Literal[
        "Snack",
        "Meal",
        "Drinks",
        "Buffet"
    ]

    vehicle_type: Literal[
        "motorcycle",
        "scooter",
        "electric_scooter",
        "bicycle"
    ]

    multiple_deliveries: int = Field(...,ge = 0,le =3)

    festival: Literal[
        "Yes",
        "No"
    ]

    city: Literal[
        "Metropolitan",
        "Urban",
        "Semi-Urban"
    ]

    order_time: str

    order_date: str

class display_result(BaseModel):
    predicted_delivery_time_min: float
    expected_min:int
    expected_max:int
    reasons: Optional[List[str]] = None