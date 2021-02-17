# Serverless ML Inference Example

### Note: This is not production code and simply meant as a demo

Serverless ML Inference Example (SMILE) is a simple solution that provides real time ML inference, while maintaing the scale-to-zero and other benefits of serverless. The example starts with local training of a simple model (Iris classification by septal/pedal size). That model is then deployed for inference using one of several options to manage the creation of the infrastructure.

To run the solution, clone/download the project. To deploy the solution follow the steps below:


## Instructions

The instructions below cover installation on Unix-based Operating systems like macOS and Linux. You can also use an AWS Cloud9 enviornment or EC2 instance to deploy the solution.

### Requirements
- Git
- Docker
- AWS CLI
- NodeJS/NPM
- AWS SAM CLI
- AWS CDK CLI

If you have not already, configure the aws cli to interact with AWS services using aws configure.

### Getting Started

If you are using Cloud9, let's clean up some disk space by removing the pre-installed Docker images:

```shell
docker rmi $(docker images -q)
```

Finally, let's upgrade the AWS CLI and AWS CDK to the latest version:

```shell
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
exec bash

npm i -g --force aws-cdk
```

You will need to clone this repo, and this example uses two CDK applications which are kept in their own repositories so you will need to initialize them:

```shell
git clone --recurse-submodules -j8 https://github.com/mikeapted/serverless-ml-inference.git

cd serverless-ml-inference
```

### Deployment

1. [Model Training](docs/model_training.md)
2. [Build/Test Our API Locally](docs/build_test_locally.md)
3. Deploy the API
    - [Deploy with the Serverless Application Model (SAM)](docs/deploy_with_sam.md)
    - [Deploy with the Cloud Development Kit (CDK) using Python](docs/deploy_with_cdk.md)
    - [Deploy with the Cloud Development Kit (CDK) using TypeScript](docs/deploy_with_cdk_typescript.md)

## Cleaning up

To avoid incurring future charges, please delete any resources in your account that you are not using such as files in Amazon S3, AWS Lambda functions, Amazon CloudWatch resources, AWS Cloud9 environments, and Amazon API Gateway entries.

## License

This project is licensed under the Apache-2.0 License.

Disclaimer: Deploying the demo applications contained in this repository will potentially cause your AWS Account to be billed for services.

## Links

- https://pypi.org/project/mangum/
- https://fastapi.tiangolo.com

- https://www.geeksforgeeks.org/deploying-ml-models-as-api-using-fastapi/
- https://faisalmalikwp.medium.com/simple-machine-learning-model-deployment-using-fastapi-5a6388db985f
- https://medium.com/analytics-vidhya/python-fastapi-and-aws-lambda-container-3e524c586f01
- https://www.betterdatascience.com/how-to-build-and-deploy-a-machine-learning-model-with-fastapi/
