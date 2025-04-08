from cancer_prediction.config.configurations import ConfigurationManager
from cancer_prediction.components.model_evaluation import Evaluation
from cancer_prediction import logger



STAGE_NAME = "MODEL_EVALUATION"


class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self) -> None:
        configuration = ConfigurationManager()
        eval_config = configuration.get_model_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        #evaluation.log_into_mlflow()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e