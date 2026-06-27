class VectorStore:

    def __init__(self): 
        self.documents = []
    def add_documents(self,chunks,embeddings):

        for chunk_id , (chunks , embeddings) in enumerate(zip(chunks,embeddings),start=1):
            document = {
                "chunk" :chunks,
                "embedding":embeddings,
                "metadata":{
                    "chunk_id":chunk_id
                }
            }

            self.documents.append(document)

    def get_documents(self):
        return self.documents



