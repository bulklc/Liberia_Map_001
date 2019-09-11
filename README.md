

docker build -t gcr.io/unified-academy-252221/liberia .
docker push gcr.io/unified-academy-252221/liberia
kubectl set image deployment/liberia-app liberia=gcr.io/unified-academy-252221/liberia:latest 

kubectl create secret generic cloudsql-db-credentials --from-env-file=./secrets/secrets.env
kubectl create secret generic cloudsql-instance-credentials --from-file=credentials.json=./secrets/unified-academy-252221-b53c35df2dad.json

