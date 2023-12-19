### windows

```
choco install kubernetes-helm
```

### macos

```
brew install helm
```

# Kubernetes Dashboard

-> Add kubernetes-dashboard repository

```
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
```

-> Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart

```
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

# Pod Forwarding

-> Pod Name kriegen

```
kubectl get pods -n kubernetes-dashboard
```

-> Pod forwording

```
kubectl
```

-> Token kriegen

```
kubectl apply -f config.yml
```

```
kubectl -n kubernetes-dashboard create token admin-user
```