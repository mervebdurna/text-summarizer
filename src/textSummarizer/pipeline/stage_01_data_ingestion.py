from textSummarizer.logging import logger
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()