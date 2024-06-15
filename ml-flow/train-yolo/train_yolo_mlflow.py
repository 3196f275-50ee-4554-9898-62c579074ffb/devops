import mlflow
import mlflow.pyfunc
from mlflow import log_metric, log_param, log_artifacts
import os
from ultralytics import YOLO

def train_yolo(data_path, epochs=50, img_size=640):
    # Настройка MLflow
    mlflow.set_tracking_uri("http://192.168.0.18:5000")
    mlflow.set_experiment("YOLO Pose Detection")

    with mlflow.start_run():
        # Логирование параметров
        log_param("data_path", data_path)
        log_param("epochs", epochs)
        log_param("img_size", img_size)

        # Загрузка модели
        model = YOLO("yolov5s.pt")

        # Тренировка модели
        results = model.train(data=data_path, epochs=epochs, imgsz=img_size)

        # Логирование метрик
        log_metric("box_loss", results.box_loss)
        log_metric("obj_loss", results.obj_loss)
        log_metric("cls_loss", results.cls_loss)
        log_metric("precision", results.precision)
        log_metric("recall", results.recall)
        log_metric("mAP_0.5", results.map_50)
        log_metric("mAP_0.5:0.95", results.map)

        # Сохранение модели
        model_path = "yolov5_model"
        model.save(model_path)

        # Логирование артефактов
        log_artifacts(model_path)

if __name__ == "__main__":
    data_path = "/path/to/your/dataset.yaml"
    train_yolo(data_path)