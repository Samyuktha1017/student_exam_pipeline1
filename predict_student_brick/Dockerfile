FROM python:3.9-slim

WORKDIR /app

COPY predict_student.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "predict_student.py"]
