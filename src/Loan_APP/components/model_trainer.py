import pandas as pd
from Loan_APP.config.configuration import ModelTrainerConfig
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = train_data[[self.config.target_column]]
        
        model = RandomForestClassifier(n_estimators= self.config.n_estimators, min_samples_split= self.config.min_samples_split, min_samples_leaf= self.config.min_samples_split, max_samples= self.config.max_samples, max_leaf_nodes= self.config.max_leaf_nodes, max_depth= self.config.max_depth, max_features= self.config.max_features, class_weight= self.config.class_weight, oob_score= self.config.oob_score, random_state= self.config.random_state)
        model.fit(train_x, train_y)
        
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        