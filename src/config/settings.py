from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
APP_NAME = os.getenv("APP_NAME")  # Default to "MyApp" if not set
