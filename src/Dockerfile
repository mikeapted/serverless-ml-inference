FROM amazon/aws-lambda-python:3.8

ARG model_path=./iris_model.pkl

COPY *.py ./
COPY $model_path /
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/lambda-entrypoint.sh"]
CMD ["main.handler"]
