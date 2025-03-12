from Loan_APP.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from Loan_APP import logger
import pandas as pd
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # We can add all type of data transformation technique here. like PCA, Scaler, EDA
    
    def data_cleaning(self):
        data = pd.read_csv(self.config.data_path)
        data.drop('loan_id', axis =1 , inplace = True)
        
        nan_cat_feature = ['gender', 'married', 'self_employed', 'credit_history']
        for col in nan_cat_feature:
            # data[col].fillna(data[col].mode()[0], inplace = True)
            data.fillna({col: data[col].mode()[0]}, inplace= True)
            
        nan_cont_feature = ['dependents', 'loanamount', 'loan_amount_term']
        for col in nan_cont_feature:
            # data[col].fillna(data[col].median(), inplace = True)
            data.fillna({col: data[col].median()}, inplace=True)
            
        # print(data.isnull().sum())
        
        df_obj = data.select_dtypes('O')
        
        lbl_ecoder = LabelEncoder()
        for col in df_obj:
            data[col] = lbl_ecoder.fit_transform(data[col])
        
        # print(data.head())
        
        return data
        
    def train_test_spliting(self, data):
        # data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data, test_size=0.2, random_state= 42)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        # print(train.shape)
        # print(test.shape)
    
    