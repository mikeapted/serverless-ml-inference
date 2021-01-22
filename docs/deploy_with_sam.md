# Deploy with SAM

### Build

First we will build our Docker image using SAM, and generate our deployment template:

```shell
sam build
```

### Test Locally

We can test the new container locally using the SAM CLI:

```shell
sam local invoke -e ../events/event.lambda.root.json
sam local invoke -e ../events/event.lambda.name.json
sam local invoke -e ../events/event.lambda.predict.json
```

or we can stand up a local version of the API to test directly:

```shell
sam local start-api

curl http://localhost:3000/ 

curl -d @event.container.predict.json \
    -H "Content-Type: application/json" \
    -X POST http://localhost:3000/invocations
```
### Deploy

```shell
sam deploy --guided
```

## Test

We can now test our deployed endpoint:

```shell
export SAM_URL=<URL from the SAM deployment output>

curl "${SAM_URL}/"

curl "${SAM_URL}/mike"

curl -X POST -H "Content-Type: application/json" \
  -d @../events/event.container.predict.json "${SAM_URL}/predict"
```

### View the Logs

```shell
sam logs -n MyApiInferenceFunction --stack-name my-api --tail
sam logs -n MyApiInferenceFunction --stack-name my-api -s '10min ago' -e '2min ago'
sam logs -n MyApiInferenceFunction --stack-name my-api --filter "sepal_length"
```