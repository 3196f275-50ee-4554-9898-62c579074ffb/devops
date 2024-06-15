FROM ghcr.io/mlflow/mlflow:v2.0.1

WORKDIR /app

COPY . /app

RUN pip install ultralytics mlflow

CMD ["python", "train_yolo_mlflow.py"]