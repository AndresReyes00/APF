from app.schemas.measurement import MeasurementResponse
from fastapi import APIRouter, Query
from typing import Literal

router = APIRouter(
    prefix="/api/measurements",
    tags=["Measurements"],
)

# Datos sintéticos para desarrollo.
# No representan mediciones médicas reales.
SAMPLE_MEASUREMENTS = [
    {
        "id": 1,
        "subject_id": "TEST-001",
        "metric": "heart_rate",
        "value": 72,
        "unit": "bpm",
        "measured_at": "2026-10-20T10:00:00",
        "source": "synthetic",
    },
    {
        "id": 2,
        "subject_id": "TEST-001",
        "metric": "heart_rate",
        "value": 76,
        "unit": "bpm",
        "measured_at": "2026-10-20T10:05:00",
        "source": "synthetic",
    },
    {
        "id": 3,
        "subject_id": "TEST-001",
        "metric": "spo2",
        "value": 98,
        "unit": "%",
        "measured_at": "2026-10-20T10:00:00",
        "source": "synthetic",
    },
]


@router.get("", response_model=MeasurementResponse)
def get_measurements(
        subject_id: str | None = Query(default=None, min_length=1),
        metric: Literal["heart_rate", "spo2"] | None = Query(default=None),
    ):

    filtered_measurements = [
        measurement for measurement in SAMPLE_MEASUREMENTS
        if (subject_id is None or measurement["subject_id"] == subject_id) and
           (metric is None or measurement["metric"] == metric)
    ]   


    return {
        "items": filtered_measurements,
        "total": len(filtered_measurements),
        "message": "Synthetic development data"
    }