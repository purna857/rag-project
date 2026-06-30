import os 
import google.generativeai as genai 
from dotenv import load_dotenv 

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class LLMService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    

    def generate_answer(self,prompt):
        response = self.model.generate_content(prompt) 


        return response.text