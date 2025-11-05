# translate-genomas

docker build -t translate-api-genomas .
docker run -d -p 8000:8000 translate-api-genomas
docker logs -f <container_id>


## 

pip install awscli
pip install aws-sam-cli
