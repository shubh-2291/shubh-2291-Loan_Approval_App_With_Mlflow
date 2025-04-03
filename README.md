# Loan Approval App with MLflow

## Overview
The **Loan Approval App** is a machine learning-based application designed to predict loan approvals based on various applicant details. The project integrates **MLflow** for tracking and managing the machine learning lifecycle, ensuring model reproducibility and performance monitoring.

## Features
- **Machine Learning Model**: Uses a predictive model to determine loan approval.
- **MLflow Integration**: Tracks model parameters, metrics, and artifacts.
- **Flask API**: Exposes endpoints for loan prediction.
- **Frontend Interface**: Simple UI for users to input applicant details.
- **Docker Support**: Containerized deployment using Docker.

## Tech Stack
- **Programming Language**: Python
- **Machine Learning**: Scikit-learn
- **Model Tracking**: MLflow, DAGsHub
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite/PostgreSQL (if applicable)
- **Containerization**: Docker

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip
- Virtual environment (optional but recommended)
- Docker (optional for containerized deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shubh-2291/shubh-2291-Loan_Approval_App_With_Mlflow.git
   cd Loan_Approval_App_With_Mlflow
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source venv/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run MLflow tracking server (if using locally):
   ```bash
   mlflow ui --port 5000
   ```
5. Start the Flask app:
   ```bash
   python app.py
   ```
6. Access the UI at:
   ```
   http://127.0.0.1:8080
   ```

## Usage
1. Open the web interface.
2. Enter applicant details.
3. Click on "Predict" to check loan approval status.
4. View MLflow dashboard to monitor model performance.

## Deployment
### Docker
1. Build the Docker image:
   ```bash
   docker build -t loan-approval-app .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 loan-approval-app
   ```

### Cloud Deployment (Optional)
- Deploy on **AWS**.
- Use **CI/CD pipelines** for automated deployment.

## MLflow Tracking
- **Experiments**: Logs model versions, parameters, and metrics.
- **Artifact Store**: Stores model files and experiment data.
- **Comparison**: Compare different models and track performance.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push to your branch.
4. Open a pull request.

## License
This project is licensed under the **MIT License**.

## Contact
For any queries, contact:
- **GitHub**: [shubh-2291](https://github.com/shubh-2291)


<!-- # ML_Project

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
 - Logging & tagging your model -->
