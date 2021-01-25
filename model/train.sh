docker build -t training .
docker run --rm -it -v $(pwd):/tmp training
docker image rm training