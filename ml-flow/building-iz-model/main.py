import os
import mlflow
import mlflow.pytorch
from ultralytics import YOLO
import tempfile
import shutil

# Путь к файлу с весами
model_path = os.path.expanduser('./YOLOMLSHIT/best.pt')

# Загрузка модели YOLO
model = YOLO(model_path)

# Установка URI для отслеживания
mlflow.set_tracking_uri('http://192.168.0.18:5000')
mlflow.set_experiment('YOLO ТБ')

# Директория для артефактов
artifact_dir = os.path.expanduser('./mlflow_artifacts')

if not os.path.exists(artifact_dir):
    os.makedirs(artifact_dir)

# Установка переменной окружения для артефактов MLflow
os.environ['MLFLOW_ARTIFACT_ROOT'] = artifact_dir

with mlflow.start_run() as run:
    # Временная директория для хранения модели
    temp_model_dir = tempfile.mkdtemp()

    # Сохранение модели в временную директорию
    model_save_path = os.path.join(temp_model_dir, "model")
    mlflow.pytorch.save_model(model, path=model_save_path)

    # Логирование артефактов модели из временной директории в артефакты MLflow
    mlflow.log_artifacts(temp_model_dir, artifact_path="model")

    # Регистрация модели
    mlflow.register_model(f"runs:/{run.info.run_id}/model", "YOLOModel")

    # Удаление временной директории после логирования
    shutil.rmtree(temp_model_dir)

print("Model registered successfully!")