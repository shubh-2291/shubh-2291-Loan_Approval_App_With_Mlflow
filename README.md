# ML_Project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in the src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

# How to run?

### STEPS:
 Clone the repository

 ```bash
https://github.com/shubh-2291/shubh-2291-Loan_Approval_App_With_Mlflow
```
### STEP 01- Create a virtual environment after opening the repository

```bash
virtualenv env
```
#### Note: if virtualenv not installed , intalled it.
```bash
pip install virtualenv
```
### step 02- activate virtual environment
```bash
env/Scripts/activate
```
### step 03- install the requirements
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
Now,
``` bash
open up your host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/shubh-2291/shubh-2291-Loan_Approval_App_With_Mlflow.mlflow

MLFLOW_TRACKING_USERNAME=shubh-2291

MLFLOW_TRACKING_PASSWORD=bda8667039f829190ef0956963cf5992817e71f0
python script.py

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/shubh-2291/shubh-2291-Loan_Approval_App_With_Mlflow.mlflow

set MLFLOW_TRACKING_USERNAME=shubh-2291

set MLFLOW_TRACKING_PASSWORD=bda8667039f829190ef0956963cf5992817e71f0

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 863518422549.dkr.ecr.ap-south-1.amazonaws.com/loan_app

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = loan_app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
