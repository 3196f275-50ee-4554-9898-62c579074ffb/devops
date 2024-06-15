# ML Flow - Train Yolo model

```bash
docker build -t yolo-train-mlflow .
```

```bash
kubectl apply -f yolo-train-job.yaml
```

```bash
kubectl get jobs -n mlflow
kubectl logs job/yolo-train -n mlflow
```