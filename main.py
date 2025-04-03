from Loan_APP import logger
from Loan_APP.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Loan_APP.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Loan_APP.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Loan_APP.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from Loan_APP.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access them securely
mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
mlflow_username = os.getenv("MLFLOW_TRACKING_USERNAME")
mlflow_password = os.getenv("MLFLOW_TRACKING_PASSWORD")

# Set environment variables
os.environ["MLFLOW_TRACKING_URI"] = mlflow_tracking_uri
os.environ["MLFLOW_TRACKING_USERNAME"] = mlflow_username
os.environ["MLFLOW_TRACKING_PASSWORD"] = mlflow_password


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Stage {STAGE_NAME} Started!")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} finished!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e