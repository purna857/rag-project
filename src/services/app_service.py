from config.settings import APP_NAME
from utils.logger import logger


def start_application():
    logger.info("RAG application has started.")

    try:
        10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    finally:
        logger.info(
            f"{APP_NAME} application has stopped."
        )  # Log when the application stops
