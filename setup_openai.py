import os
from dotenv import dotenv_values

def set_env():
    os.environ["OPENAI_API_KEY"] = dotenv_values(".env")['LLM_KEY']

set_env()
def reset_env():    
    os.environ.pop('OPENAI_API_KEY')
