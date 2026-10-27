
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, measurements

app = FastAPI(
    title="Space Health API",
    description="API for the Space Health Monitoring Dashboard",
    version="0.1.0",
)

# Permitir que React/Vite se comunique con FastAPI durante el desarrollo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(measurements.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Space Health API",
        "docs": "/docs",
    }
