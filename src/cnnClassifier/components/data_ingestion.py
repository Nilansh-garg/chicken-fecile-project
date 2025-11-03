import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        
    def download_file_1(self):
        if not os.path.exists(self.config.local_data_file_1):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL_1,
                filename = self.config.local_data_file_1
            )
            
            logger.info(f"{filename} download! with following info: \n {headers}")
            
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file_1))}")
            
            
    def download_file_2(self):
        if not os.path.exists(self.config.local_data_file_2):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL_2,
                filename = self.config.local_data_file_2
            )
                
            logger.info(f"{filename} download! with following info: \n {headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file_2))}")

            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        function
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file_1,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"extracted to {unzip_path}")
            
        with zipfile.ZipFile(self.config.local_data_file_2,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"extracted to {unzip_path}")

            
    