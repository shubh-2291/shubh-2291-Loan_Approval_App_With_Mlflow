from Loan_APP.entity.config_entity import ModelEvaluationConfig
from Loan_APP.utils.common import save_json
from urllib.parse import urlparse
from pathlib import Path
import pandas as pd
import joblib
import mlflow
import os

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    # def eval_metric(self, actual, pred):
    #     rmse = np.sqrt(mean_squared_error(actual, pred))
    #     mae = mean_absolute_error(actual, pred)
    #     r2 = r2_score(actual, pred)
    #     return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_value = model.predict(test_x)
            model_score = model.score(test_x, test_y)
            oob_score = model.oob_score_
            # confusion_matrix = confusion_matrix(test_y, predicted_value)
            scores = {"model_score":model_score, "oob_score": oob_score}
            save_json(path= Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("model_score",model_score )
            mlflow.log_metric("oob_score",oob_score )
            # mlflow.log_metric("confusion_matrix",confusion_matrix)
            
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name= "RandomForestModel")
            else:
                mlflow.sklearn.log_model(model, "model")