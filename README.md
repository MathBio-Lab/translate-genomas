# translate-genomas

docker build -t translate-api-genomas .
docker run -d -p 8000:8000 translate-api-genomas
docker logs -f <container_id>


## 

pip install awscli
pip install aws-sam-cli


## 

docker build --platform linux/amd64 -t


## 

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <link-repo>


## 

docker tag translate-genomas:latest <link-repo>/genomas/translate-genomas:latest

## 
docker push <link-repo>/genomas/translate-genomas:latest


## todo en uno

docker buildx build --platform linux/amd64 -t <link-repo>:latest --push .


## probar y subir

docker build -t mi-lambda-local .

docker run --rm -p 9000:8080 \
  -v ~/.aws:/root/.aws:ro \
  mi-lambda-local

el curl:

```bash

curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{
    "version": "2.0",
    "routeKey": "$default",
    "rawPath": "/translate/",
    "rawQueryString": "",
    "headers": {
        "accept": "application/json",
        "content-type": "application/json",
        "user-agent": "curl/7.81.0"
    },
    "requestContext": {
        "http": {
            "method": "POST",
            "path": "/translate/",
            "protocol": "HTTP/1.1",
            "sourceIp": "127.0.0.1",
            "userAgent": "curl/7.81.0"
        },
        "requestId": "local-test-translate",
        "routeKey": "$default",
        "stage": "$default",
        "timeEpoch": 1672531200
    },
    "body": "{\"text\": \"Hello, what a wonderful day!\", \"source_language\": \"en\", \"target_language\": \"es\"}",
    "isBase64Encoded": false
}'

```

logar y docker buildx build --platform linux/amd64 -t <link-repo> --push .