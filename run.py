""" Running the Xetra ETL Application """

import logging
import logging.config
import yaml

def main():
    """
    Entry point to run the Xetra ETL Job
    """

    # Parsing YAML file
    config_path = 'C:/ETL Pipelines in Python/xetra_project/xetra_1234/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    #__name__ is the name of the file
    logger = logging.getLogger(__name__)
    logger.info("This is a test!")

if __name__ == '__main__':
    main()