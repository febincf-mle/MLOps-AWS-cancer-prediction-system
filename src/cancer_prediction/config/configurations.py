import os

from cancer_prediction.constants import *
from cancer_prediction.utils import read_yaml, create_directories
from cancer_prediction.entity.config_entity import (DataIngestionConfig, 
                                                    PrepareBaseModelConfig,
                                                    ModelTrainerConfig,
                                                    ModelEvaluationConfig
                                                    )


class ConfigurationManager:

    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):

        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE,
            params_num_epochs=params.NUM_EPOCHS,
            params_learning_rate=params.LEARNING_RATE,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES,
            params_include_top=params.INCLUDE_TOP
        )

        return prepare_base_model_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        training_config = self.config.training
        prepare_base_model_config = self.config.prepare_base_model

        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'data', 'chest-ct-scan-data')

        create_directories([
            Path(training_config.root_dir)
        ])

        training_config_entity = ModelTrainerConfig(
            root_dir=Path(training_config.root_dir),
            trained_model_path=Path(training_config.trained_model_path),
            updated_base_model_path=Path(prepare_base_model_config.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.NUM_EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config_entity
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        training_config = self.config.training
        data_ingestion_config = self.config.data_ingestion

        eval_config = ModelEvaluationConfig(
            path_of_model=Path(training_config.trained_model_path),
            training_data=os.path.join(data_ingestion_config.unzip_dir, 'data', 'chest-ct-scan-data'),
            mlflow_uri=None,
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )

        return eval_config