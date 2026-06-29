from utils.similarity import cosine_similarity


class Retriever:
    """
       Responsible for retrieving documents from the Vectore Store
       (First Version) 
    """

    def __init__(self,vector_store,embedding_service):
        self.vector_store = vector_store 
        self.embedding_service = embedding_service  
    

    def retrieve(self,query):
        query_embedding = self.embedding_service.generate_embeddings([query])[0] 

        documents = self.vector_store.get_documents() 

        best_score = -1 
        best_document = None 

        for document in documents:

            similarity = cosine_similarity(query_embedding,document["embedding"])

            if similarity > best_score:
                best_score = similarity 
                best_document = document 

        return best_document 