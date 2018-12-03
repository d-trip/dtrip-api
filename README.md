# dtrip-api
Api server for DTrip apps.

## Run in Docker:
```
docker run -d --name dtrip-api -t -d \
  -e MONGO_HOST= \
  -e MONGO_USERNAME= \
  -e MONGO_PASSWORD= \
  -p 5000:5000 avral/dtrip-api
```
