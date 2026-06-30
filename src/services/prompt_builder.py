class PromptBuilder:
    """
      Resposible for creating LLM Prompts 
    """

    def build_prompt(self,context,question):
        prompt = f""" 
        You are a helpful AI assistant.
        
        Use only the following context to answer the user's question.
        
        Context:
        {context}
        
        Question:
        {question}
        
        Answer: 
"""
        return  prompt