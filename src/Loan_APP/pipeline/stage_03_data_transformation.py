from Loan_APP.config.configuration import ConfigurationManager
from Loan_APP.components.data_transformation import DataTransformation
from pathlib import Path
from Loan_APP import logger

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                cleaned_df = data_transformation.data_cleaning()
                data_transformation.train_test_spliting(cleaned_df)
            else:
                raise Exception("Data Schema is not valid")
            
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} Started!")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} finished!")
    except Exception as e:
        logger.exception(e)
        raise e