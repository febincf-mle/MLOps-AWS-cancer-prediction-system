from src.cancer_prediction.config.configurations import ConfigurationManager
from src.cancer_prediction.components.data_ingestion import DataIngestion
from src.cancer_prediction import logger



STAGE_NAME = "DATA_INGESTION"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass


    def main(self) -> None:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e