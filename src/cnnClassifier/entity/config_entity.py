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