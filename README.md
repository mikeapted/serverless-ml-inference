# Serverless ML Inference Example

Serverless ML Inference Example (SMILE) is a simple solution that provides real time ML inference, while maintaing the scale-to-zero and other benefits of serverless. The example starts with local training of a simple model (Iris classification by septal/pedal size). That model is then deployed for inference using one of several options to manage the creation of the infrastructure.

To run the solution, clone/download the project. To deploy the solution follow the steps below:


## Instructions

The instructions below cover installation on Unix-based Operating systems like macOS and Linux. You can alos use an AWS Cloud9 enviornment or EC2 instance (recommended: t3.large or higher on Amazon Linux platform) to deploy the solution.

### Requirements
- Git
- Docker
- aws cli
- node/npm
- AWS SAM
- AWS CDK

If you have not already, configure the aws cli to interact with AWS services using aws configure.

### Deployment

1. [Model Training](docs/model_training.md)
2. [Build/Test Our API Locally](docs/build_test_locally.md)
3. Deploy the API
    - [Deploy with the Serverless Application Model (SAM)](docs/deploy_with_sam.md)
    - [Deploy with the Cloud Development Kit (CDK)](docs/deploy_with_cdk.md)

## Cleaning up

To avoid incurring future charges, please delete any resources in your account that you are not using such as files in Amazon S3, Amazon ECS and Amazon Lambda instances, AWS Cloud9 environment and Amazon API Gateway entries.

## License

This project is licensed under the Apache-2.0 License.

Disclaimer: Deploying the demo applications contained in this repository will potentially cause your AWS Account to be billed for services.

## Links

https://pypi.org/project/mangum/
https://fastapi.tiangolo.com


https://www.geeksforgeeks.org/deploying-ml-models-as-api-using-fastapi/
https://faisalmalikwp.medium.com/simple-machine-learning-model-deployment-using-fastapi-5a6388db985f
https://medium.com/analytics-vidhya/python-fastapi-and-aws-lambda-container-3e524c586f01
https://www.betterdatascience.com/how-to-build-and-deploy-a-machine-learning-model-with-fastapi/
