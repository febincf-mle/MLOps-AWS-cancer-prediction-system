from cancer_prediction.config.configurations import ConfigurationManager
from cancer_prediction.components.prepare_base_model import PrepareBaseModel
from cancer_prediction import logger



STAGE_NAME = "PREPARE_BASE_MODEL"


class PrepareBaseModelPipeline:

    def __init__(self):
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        prepare_base_model_component = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model_component.get_base_model()
        prepare_base_model_component.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = PrepareBaseModelPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e