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


docker run --rm -p 9000:8080 \
  -e ENVIRONMENT=development \
  -e AWS_REGION=us-east-2 \
  -v ~/.aws:/root/.aws:ro \
  mi-lambda-local


# validar credenciales 

docker exec -it $(docker ps -q -f publish=9000) bash


python - <<'PYCODE'
import boto3, json
try:
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    print("✅ Credenciales detectadas correctamente:")
    print(json.dumps(identity, indent=2))
except Exception as e:
    print("❌ No se detectaron credenciales:", e)
PYCODE



# verificar servicio

python - <<'PYCODE'
import boto3
translate = boto3.client("translate", region_name="us-east-2")
result = translate.translate_text(
    Text="Hello world!",
    SourceLanguageCode="en",
    TargetLanguageCode="es"
)
print("✅ Traducción:", result["TranslatedText"])
PYCODE




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


ANY /{proxy+}

$default 