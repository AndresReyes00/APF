
from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Measurement(BaseModel):
    id: int
    subject_id: str
    metric: Literal["heart_rate", "spo2"]
    value: float
    unit: str
    measured_at: datetime
    source: Literal["synthetic"]


class MeasurementResponse(BaseModel):
    items: list[Measurement]
    total: int
    message: str
