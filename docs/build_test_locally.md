# Build an Test Locally

We will now use our model artifact to build a FastAPI container, which will serve our predictions.

### Build the API container

First, we need to copy our model artifcat from Step 1 to this directory:

```shell
cd src

cp ../model/iris_model.pkl .
```

Then we build our container:

```shell
docker build -t myapiinferencefunction .
```

### Run the API locally with just FastAPI

We can test a traditional FastAPI version of our container by overriding the ENTRYPOINT/CMD when running it:

```shell
docker run -d --entrypoint uvicorn -p 80:80 myapiinferencefunction main:app --host 0.0.0.0 --port 80
```

and then test that API using curl and standard JSON payload for the data when making a prediction:

```shell
curl "http://localhost"

curl "http://localhost/mike"

curl -X POST -H "Content-Type: application/json" \
  -d @../events/event.container.predict.json \
  "http://localhost/predict"
```

our JSON event for the prediction takes the shape:

```json
{
  "sepal_length": 5.7,
  "sepal_width": 3.1,
  "petal_length": 4.9,
  "petal_width": 2.2
}
```

### Run the API locally with Mangum wrapping FastAPI

We can test a Lambda enabled version of our container by leaving the defaults when running it:

```shell
docker run -d -p 9000:8080 myapiinferencefunction
```

and then test that API using curl and standard JSON payload for the data when making a prediction:

```shell
curl -d @../events/event.lambda.root.json \
  "http://localhost:9000/2015-03-31/functions/function/invocations"

curl -X POST -H "Content-Type: application/json" \
  -d @../events/event.lambda.predict.json \
  "http://localhost:9000/2015-03-31/functions/function/invocations"
```

Let's stop our Docker containers to free up the ports for later use:

```shell
docker stop $(docker ps -q)
```

You can now return to the project root.

```shell
cd ..
```
