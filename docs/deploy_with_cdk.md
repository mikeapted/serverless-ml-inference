# Deploy with CDK

### Bootstrap CDK

```shell
cdk bootstrap
```

?SAM Local testing?

### Deploy

```shell
cdk deploy
```

### Test

```shell
export CDK_URL=<URL from the SAM deployment output>
export CDK_LOG_GROUP=<URL from the SAM deployment output>

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

You can now return to the project root.

```shell
cd ..
```
