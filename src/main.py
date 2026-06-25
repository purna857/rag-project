from utils.logger import logger
from services.app_service import start_application
from services.document_loader import DocumentLoader
from services.text_splitter import TextSplitter

def main():
    start_application()
    loader = DocumentLoader()
    document_content = loader.load_document("docs/python_notes.txt") 
    logger.info(document_content) 
    splitter = TextSplitter()
    chunks = splitter.split_text(document_content) 
    logger.info("\n==============CHUNKS==============\n")
    for index, chunk in enumerate(chunks, start=1):
        logger.info(f"Chunk {index}")
        logger.info(chunk)
        logger.info("-" * 40)

if __name__ == "__main__":
    main()
