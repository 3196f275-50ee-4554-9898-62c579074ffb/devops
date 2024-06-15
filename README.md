# Research.Space Building

## Dev Ops repo

Команда Research.Space представляет решение для мониторингу и управлению вашими строительными объектами. В данном репозитории хранится код для развертывания серверной инфраструктуры.

## Репозиторий включает в себя

1. `k8s-kafka` - Дирректория отвечающая за арбитражную шину apache kafka
2. `Graphana` - Дирректория отвечающая за визуализацию состояния системы и бизнеса (http://localhost:3000)

```bash
minikube start
```


```bash
cd ml-flow && kubectl apply -f 00-mlflow-deployment.yaml && kubectl port-forward svc/mlflow 5000:5000 -n mlflow && cd ../
```

```bash
cd k8s-kafka && kubectl apply -f 00-namespace.yaml && kubectl apply -f 01-zookeeper.yaml && kubectl apply -f 02-kafka.yaml && kubectl get pods -n kafka
```

```bash
kubectl port-forward <pod_name> 9092 -n kafka && cd ../
```

```bash
cd graphana && kubectl create namespace monitoring && kubectl apply -f 00-grafana-config.yaml && kubectl apply -f 01-grafana-pvc.yaml && kubectl apply -f 02-grafana-deployment.yaml && kubectl apply -f 03-grafana-service.yaml && kubectl get pods -n monitoring && kubectl port-forward --namespace monitoring service/grafana 3000:80 && cd ../
```