from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_dir: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen= True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    target_column: str
    oob_score: bool
    n_estimators: int
    min_samples_split: int
    min_samples_leaf: int
    max_samples: float
    max_leaf_nodes: int
    max_depth: int
    max_features: str
    class_weight: str
    random_state: int