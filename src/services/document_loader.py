from pathlib import Path 


class DocumentLoader:


    def load_document(self,file_path:str) -> str:
        """
        Load the content of a document from the given file path.

        Args:
            file_path (str): The path to the document file.

        Returns:
            str: The content of the document.
        """
        path = Path(file_path) 

        with path.open('r',encoding='utf-8') as file:
            content = file.read()   
        return content 