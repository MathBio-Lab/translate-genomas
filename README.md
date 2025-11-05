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