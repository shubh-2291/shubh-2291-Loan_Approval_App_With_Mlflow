from Loan_APP.constants import *
from Loan_APP.utils.common import read_yaml, create_directories
from Loan_APP.entity.config_entity import DataIngestionConfig, DataValidationConfig ,DataTransformationConfig
from Loan_APP.entity.config_entity import ModelTrainerConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
        ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_dir=config.source_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema= schema
        )
        
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestClassifier
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            target_column= schema.name,
            oob_score= params.oob_score,
            n_estimators= params.n_estimators,
            min_samples_split=params.min_samples_split,
            min_samples_leaf= params.min_samples_leaf,
            max_samples= params.max_samples,
            max_leaf_nodes= params.max_leaf_nodes,
            max_depth= params.max_depth,
            max_features= params.max_features,
            class_weight= params.class_weight,
            random_state= params.random_state
        )
        
        return model_trainer_config
        
        