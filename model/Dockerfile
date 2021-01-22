FROM amazon/aws-lambda-python:3.8

COPY *.py ./
COPY *.csv ./
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["train.py"]