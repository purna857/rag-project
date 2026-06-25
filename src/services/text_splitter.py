class TextSplitter:


    def split_text(self,text:str,chunk_size:int = 2):
        """
        Split the input text into chunks of specified size.

        Args:
            text (str): The input text to be split.
            chunk_size (int): The size of each chunk. Default is 2.

        Returns:
            list: A list of text chunks.
        """
        lines = text.splitlines() 
        chunks = [] 
        for i in range(0,len(lines),chunk_size):
            chunk = "\n".join(lines[i:i+chunk_size])  
            chunks.append(chunk)
        return chunks   