from fastapi import FastAPI

app = FastAPI(
    title="NASA Astronaut Health API",
    description="API for querying astronaut physiological data",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "NASA Astronaut Health API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }