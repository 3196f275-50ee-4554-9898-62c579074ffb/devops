import mlflow
import mlflow.sklearn

# Загрузка модели по её пути в MLflow
model_uri = f"runs:/{run_id}/model"
loaded_model = mlflow.sklearn.load_model(model_uri)

# Прогнозирование с использованием загруженной модели
predictions = loaded_model.predict(X_test)
print(predictions)