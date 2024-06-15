import os
import mlflow
import mlflow.pytorch
from ultralytics import YOLO

# Путь к файлу с весами
model_path = os.path.expanduser('./YOLOMLSHIT/best.pt')

# Загрузка модели YOLO
model = YOLO(model_path)

# Настройка трекера MLflow
mlflow.set_tracking_uri('http://192.168.0.18:5000')
mlflow.set_experiment('YOLO ТБ')

# Запуск сессии MLflow
with mlflow.start_run() as run:
    # Логирование параметров
    mlflow.log_param('model_type', 'YOLOv8')

    # Сохранение файла модели
    model_save_path = 'best.pt'
    model.save(model_save_path)

    # Логирование файла модели как артефакта
    mlflow.log_artifact(model_save_path, artifact_path='models')

    print(f"Model logged in run {run.info.run_id}")