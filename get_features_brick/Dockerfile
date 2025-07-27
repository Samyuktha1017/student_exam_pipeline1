FROM python:3.9-slim

WORKDIR /app
COPY get_features.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "get_features.py"]
