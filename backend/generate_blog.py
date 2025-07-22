from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv



# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')



def generate_blog(topic):
    