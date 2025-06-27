FROM python:3.11-slim

WORKDIR /app

COPY AI_Microservice /app/AI_Microservice
COPY AI_Microservice/requirements.txt /app/requirements.txt

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "AI_Microservice.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
