from venv import logger
from config.settings import APP_NAME
from utils.logger import logger 
def start_application():
    logger.info("RAG application has started.")  # Log when the application starts

    try:
        number = 10/0  # This will raise a ZeroDivisionError
    except Exception as e:
        logger.error(f"An error occurred: {e}")  # Log the error message 

    finally:
        logger.info(f"{APP_NAME} application has stopped.")  # Log when the application stops