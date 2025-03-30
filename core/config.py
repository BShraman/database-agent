
from langchain_community.chat_models import ChatOpenAI
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from dotenv import load_dotenv
import logging
logger = logging.getLogger(__name__)
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    logging.basicConfig(level=logging.INFO) 
    logger = logging.getLogger(__name__)

    # Database connection details
    PG_USER:str = os.getenv('PG_USER', 'postgres')
    PG_PASSWORD:str = os.getenv('PG_PASSWORD', 'postgres')
    PG_HOST:str = os.getenv('PG_HOST', 'localhost')
    PG_PORT:int = os.getenv('PG_PORT', 5432)
    PG_DB:str = os.getenv('PG_DB', 'postgres')

    #LLM
    # LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-3.5-turbo')
    # LLM = ChatOpenAI(LLM_MODEL)
    # OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    LLM:str = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")

config = Config()
