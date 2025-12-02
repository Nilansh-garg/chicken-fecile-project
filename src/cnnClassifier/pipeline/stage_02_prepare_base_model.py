from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.prepare_base_model_config = self.config.get_prepare_base_model_config()
        self.prepare_base_model = PrepareBaseModel(config=self.prepare_base_model_config)

    def run(self):
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        
        # Downloading and saving the base model
        self.prepare_base_model.get_base_model()
        
        # Updating the base model
        self.prepare_base_model.update_base_model()
        
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
        

if __name__ == "__main__":
    try:
        config = ConfigurationManager()
        prepare_base_model_pipeline = PrepareBaseModelPipeline(config=config)
        prepare_base_model_pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise e