from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir:Path
    source_URL_1: str
    local_data_file_1: Path
    source_URL_2: str
    local_data_file_2: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    param_image_size: list
    param_learning_rate: float
    param_include_top: bool
    param_weights: str
    param_model_name: str
    params_classes: int
    
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_rot_log_dir:Path
    checkpoint_model_filepath:Path