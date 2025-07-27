FROM python:3.9-slim

WORKDIR /app

COPY train_model.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "train_model.py"]
