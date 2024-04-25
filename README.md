# FastAPI Backend Server

## Overview

This project is a FastAPI server application that provides backend services for a facial recognition-based ATM system. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

### Features

- **High Performance**: Comparable to NodeJS and Go thanks to Starlette and Pydantic.
- **FastAPI /docs**: Automatic interactive API documentation with Swagger UI.
- **Robust Security**: Built-in security and authentication support.
- **Data Validation**: Powerful data validation and serialization with Pydantic.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package installer)

### Setting up a Virtual Environment

It is recommended to create a virtual environment to manage the dependencies for your project and ensure that it does not impact other Python projects you're working on.

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Your virtual environment is now active.
```

### Installing Dependencies

With your virtual environment active, install the project dependencies using:

```
pip install -r requirements.txt
```

### Running the Server

To run the server locally, use the following command:

```
uvicorn main:app --reload
```

Replace **main:app** with the appropriate Python file and FastAPI app instance name. The **--reload** flag enables hot reloading during development.

The server will be available at http://localhost:8000.