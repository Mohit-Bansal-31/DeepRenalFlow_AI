from DeepRenalFlow import logger
from DeepRenalFlow.config.configuration import ConfigurationManager
from DeepRenalFlow.components.model_training import Training


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training= Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        

if __name__ == "__main__":
    try:
        logger.info(f"******************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x\n")
    except Exception as e:
        logger.exception(e)
        raise e