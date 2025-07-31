from DeepRenalFlow import logger
from DeepRenalFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from DeepRenalFlow.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from DeepRenalFlow.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx=============x\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"***************")
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx=============x\n")
    
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e