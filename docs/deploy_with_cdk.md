# Deploy with CDK using Python

### Bootstrap CDK

```shell
cd cdk-my-api-python

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cdk bootstrap
```

### Deploy

```shell
cdk deploy
```

### Test

```shell
export CDK_URL=<URL from the CDK deployment output>
export CDK_LOG_GROUP=<URL from the CDK deployment output>

curl "${CDK_URL}/"

curl "${CDK_URL}/mike"

curl -X POST -H "Content-Type: application/json" \
  -d @../events/event.container.predict.json \
  "${CDK_URL}/predict"
```

### View the Logs

```shell
aws logs tail $CDK_LOG_GROUP --follow
aws logs tail $CDK_LOG_GROUP --since 5m
aws logs tail $CDK_LOG_GROUP --filter-pattern "sepal"
```

### Cleanup

If you are done experimenting with the API you can tear down the resources by deleting the CloudFormation stack from the AWS Console, or using the command:

```shell
cdk destroy
```

You can now return to the project root.

```shell
cd ..
```
