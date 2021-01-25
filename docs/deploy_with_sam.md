# Deploy with SAM

### Build

First we will build our Docker image using SAM, and generate our deployment template:

```shell
cd sam

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

Before we deploy we need an Elastic Container Registry to house our docker images:

```shell
aws ecr create-repository --repository-name my-api-repo \
--image-tag-mutability IMMUTABLE --image-scanning-configuration scanOnPush=true
```

```shell
sam deploy --guided
```

You can accept most defaults, and supply the following parameters:

```
	Looking for config file [samconfig.toml] :  Not found

	Setting default arguments for 'sam deploy'
	=========================================
	Stack Name [sam-app]: my-sam-api
	AWS Region [us-east-1]: us-east-1
	Image Repository for MyApiInferenceFunction: XXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/my-api-repo
	  myapiinferencefunction:latest to be pushed to XXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/my-api-repo:myapiinferencefunction-XXXXXXXXXXXX-latest

	#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
	Confirm changes before deploy [y/N]: Y
	#SAM needs permission to be able to create roles to connect to the resources in your template
	Allow SAM CLI IAM role creation [Y/n]: Y
	MyApiInferenceFunction may not have authorization defined, Is this okay? [y/N]: Y
	Save arguments to configuration file [Y/n]: Y
	SAM configuration file [samconfig.toml]: 
	SAM configuration environment [default]: 
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

### Cleanup

If you are done experimenting with the API you can tear down the resources by deleting the CloudFormation stack from the AWS Console, or using the commans:

```shell

```

You can now return to the project root.

```shell
cd ..
```
