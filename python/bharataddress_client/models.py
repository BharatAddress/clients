from pydantic import BaseModel, Field
from typing import List, Optional


class Geometry(BaseModel):
    type: str = Field(default="Point")
    coordinates: List[float]


class AddressProperties(BaseModel):
    ulb_lgd: str
    street_name: str
    house_number: str
    locality: str
    city: str
    state: str
    pin: str
    primary_digipin: str
    quality: Optional[str] = None


class AddressFeature(BaseModel):
    type: str = Field(default="Feature")
    properties: AddressProperties
    geometry: Geometry
