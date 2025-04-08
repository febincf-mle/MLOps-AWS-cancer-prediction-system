from cancer_prediction.config.configurations import ConfigurationManager
from cancer_prediction.components.model_trainer import ModelTrainer
from cancer_prediction import logger



STAGE_NAME = "MODEL_TRAINING"


class ModelTrainerPipeline:

    def __init__(self):
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.get_base_model()
        model_trainer.train_valid_generator()
        model_trainer.train()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e