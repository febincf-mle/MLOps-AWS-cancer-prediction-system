import os
import gdown
import zipfile

from cancer_prediction import logger
from cancer_prediction.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self) -> None:

        try:

            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)

            file_id = dataset_url.split("/")[-2]
            logger.info(f"Downloading file from: {dataset_url} into {zip_download_dir}")
            prefix = "https://drive.google.com/uc?/export=download&id="

            gdown.download(f"{prefix}{file_id}", zip_download_dir, quiet=False)
            logger.info(f"Downloaded file: {zip_download_dir}")

        except Exception as e:
            raise e
        

    def extract_zipfile(self) -> None:

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted file into: {unzip_path}")