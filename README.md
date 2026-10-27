# MVP: Astronaut Physiological Baseline Forecasting

## Project Overview

This project aims to develop an API for analyzing astronaut physiological data and establishing baseline measurements to support future forecasting and health-state analysis.

The backend is built with **FastAPI**, providing a modular structure that can be extended as the project evolves.

## Project Structure

- **`main.py`**: Creates the FastAPI application and registers the API routers.
- **`health.py`**: Defines a health-check endpoint to verify that the backend is running correctly.
- **`measurements.py`**: Will contain the endpoints for accessing and managing physiological measurements.
- **`__init__.py`**: Marks a directory as a Python package and can be left empty if no package initialization is required.

## How to Get Started

### 1. Clone the Repository

Clone this repository and navigate to the project directory.

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace `<repository-url>` and `<repository-folder>` with your repository URL and project directory name.

### 2. Create a Virtual Environment

Create an isolated Python environment in the project root:

```bash
python -m venv .venv
```

Activate the environment:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the project dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` exists in the project root and includes FastAPI and any other required packages.

### 4. Start the Development Server

Run the application using the FastAPI development server:

```bash
fastapi dev
```

If FastAPI cannot automatically detect the application entry point, specify the file explicitly:

```bash
fastapi dev app/main.py
```

Adjust the path to match your project structure.

### 5. Explore the API

Once the server is running, the API will be available locally. You can explore its endpoints through the interactive documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Development Status

This project is under active development. The initial focus is on establishing the API structure and implementing health-check and physiological measurement endpoints. Forecasting capabilities will be developed as the data pipeline and analytical components take shape.