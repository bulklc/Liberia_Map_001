
```bash
docker build -t gcr.io/unified-academy-252221/liberia:latest .
docker push gcr.io/unified-academy-252221/liberia:latest

# Update deployment
kubectl rollout restart deployment liberia-deployment
# Kill the other pod taking up to much space/resources. If we had more money, we could just 
# increase size of node.
kubectl get pods | awk '/liberia.*Running/{print $1}' | xargs kubectl delete pod

or kubectl apply -f deployment.yml

# Delete old pods if need be
kubectl exec liberia-deployment-85b95b779-nvqtl python manage.py migrate

kubectl set image deployment/liberia-app liberia=gcr.io/unified-academy-252221/liberia:latest 
kubectl create secret generic cloudsql-db-credentials --from-env-file=./secrets/secrets.env
kubectl create secret generic cloudsql-instance-credentials --from-file=credentials.json=./secrets/unified-academy-252221-b53c35df2dad.json
```
