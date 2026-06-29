from utils.logger import logger
from services.app_service import start_application
from services.document_loader import DocumentLoader
from services.text_splitter import TextSplitter
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore
from services.retriever import Retriever

def main():
    start_application()

    #Load the document
    loader = DocumentLoader()
    document_content = loader.load_document("docs/python_notes.txt") 
   
    #Split the document into chunks
    splitter = TextSplitter()
    chunks = splitter.split_text(document_content) 
    

    #Generate embeddings for each chunk
    embedding_service = EmbeddingService()  
    embeddings = embedding_service.generate_embeddings(chunks) 


    logger.info("\n==============CHUNKS==============\n")
    for chunk in chunks:
        logger.info(f"{chunk}\n")

    logger.info("\n==============EMBEDDINGS==============\n") 

    for embedding in embeddings:
        logger.info(f"{embedding}\n") 
        logger.info(f"Dimension {len(embedding)}") 
        logger.info("-"*50)
    # Step 4 : Store in VectorStore
    vector_store = VectorStore()
    vector_store.add_documents(chunks, embeddings)

    # Step 5 : Retrieve stored documents
    documents = vector_store.get_documents()

    # Print everything
    for document in documents:
        logger.info("=" * 80)
        logger.info("Chunk:")
        logger.info(document["chunk"])
        logger.info("\nEmbedding Dimension:")
        logger.info(len(document["embedding"]))
        logger.info("\nMetadata:")
        logger.info(document["metadata"]) 
    
    #step 6:
    retriever =  Retriever(vector_store,embedding_service)  
    query = input('Enter Your Question: ') 
    result = retriever.retrieve(query) 
    logger.info(result["chunk"])

      
if __name__ == "__main__":
    main()