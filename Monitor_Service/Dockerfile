FROM python:3.11-slim

WORKDIR /app

COPY Monitor_Service /app/Monitor_Service
COPY Monitor_Service/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "Monitor_Service/main.py"]
