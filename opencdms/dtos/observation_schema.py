# TODO: replace DTOs with pydantic.dataobject decorators on main domain model
from decimal import Decimal
from pydantic import BaseModel,UUID4
from typing import NewType, Optional, List, Dict, Any
from datetime import datetime

from opencdms.db.types import Geography, Coordinates

class CreateObservationSchema(BaseModel):
    version: int
    change_date: datetime
    phenomenon_end: datetime
    result_value: float
    comments: str
    host_id: str
    observer_id: Optional[str] = ""
    collection_id: Optional[str] = ""   
    feature_of_interest_id: Optional[str] = ""
    report_id: Optional[str] = ""
    user_id: Optional[str] = None
    status_id: Optional[int] = None
    source_id: Optional[str] = None
    observed_property_id: Optional[int] = None
    parameter: Optional[dict] = None
    elevation: float = None
    observation_type_id: Optional[int] = None
    phenomenon_start: Optional[datetime] = None
    result_uom: Optional[str] = ""
    result_description: Optional[str] = ""
    result_quality: Any #Optional[dict] = None
    result_time: Optional[datetime] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    observing_procedure_id: Optional[int] = None

class UpdateObservationSchema(BaseModel):
    location: Geography
    version: int
    change_date: datetime
    phenomenon_end: datetime
    result_value: float
    comments: str
    host_id: str
    observer_id: Optional[str] = ""
    collection_id: Optional[str] = ""
    feature_of_interest_id: Optional[str] = ""
    report_id: Optional[str] = ""
    user_id: Optional[int] = None
    status_id: Optional[int] = None
    source_id: Optional[int] = None
    observed_property_id: Optional[int] = None
    parameter: Optional[dict] = None
    elevation: float = None
    observation_type_id: Optional[int] = None
    phenomenon_start: Optional[datetime] = None
    result_uom: Optional[str] = ""
    result_description: Optional[str] = ""
    result_quality: Optional[dict] = None
    result_time: Optional[datetime] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    observing_procedure_id: Optional[int] = None


class ObservationSchema(CreateObservationSchema):
    id : str
    coordinates: Optional[Coordinates] = Coordinates(longitude=0, latitude=0)
    class Config:
        orm_mode = True


class GeometrySchema(BaseModel):
    type: str = "Point"
    coordinates: List[float]


class ObservationPygeoapiSchema(BaseModel):
    type: str = "Feature"
    geometry: GeometrySchema
    properties: ObservationSchema
    id: str
    links: List[Dict[str, str]]
