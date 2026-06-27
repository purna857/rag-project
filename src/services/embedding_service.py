from sentence_transformers import SentenceTransformer 

class EmbeddingService:
    """Responsible for converting text chunks into embedding vectors 
    using a predefined sentence Transformer Model""" 


    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")  

    def generate_embeddings(self,chunks):
        embeddings = self.model.encode(chunks)
        
        return embeddings
