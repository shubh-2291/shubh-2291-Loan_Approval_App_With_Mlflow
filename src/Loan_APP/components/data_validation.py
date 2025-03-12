from Loan_APP.entity.config_entity import DataValidationConfig
import pandas as pd
import os


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            # print(self.config.unzip_data_dir)
            # print(all_cols)
            # print(all_schema)
            
            for col in all_cols:
                if col not in all_schema:
                    # print(col, "False")
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validation_status}")
                        break
                else:
                    # print(col, "True")
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validation_status}")
            # print(validation_status)
            return validation_status
        except Exception as e:
            raise e