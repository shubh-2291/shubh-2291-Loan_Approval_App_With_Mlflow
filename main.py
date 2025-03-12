from Loan_APP import logger
from Loan_APP.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Loan_APP.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Loan_APP.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

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