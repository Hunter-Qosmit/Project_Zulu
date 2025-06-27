FROM python:3.11-slim

WORKDIR /app

COPY Dummy_Backend /app/Dummy_Backend
COPY Dummy_Backend/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "Dummy_Backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
