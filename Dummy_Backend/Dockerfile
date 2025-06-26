# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files into the container
COPY Dummy_Backend /app/Dummy_Backend
COPY requirements.txt /app/

# Set environment variable for production use
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command
CMD ["uvicorn", "Dummy_Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
