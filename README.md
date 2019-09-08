

docker build -t gcr.io/unified-academy-252221/liberia .
docker push gcr.io/unified-academy-252221/liberia
kubectl set image deployment/liberia-app liberia=gcr.io/unified-academy-252221/liberia:latest 


