import os
from dotenv import dotenv_values

def set_env():
    os.environ["OPENAI_API_KEY"] = dotenv_values(".env")['LLM_KEY']
set_env()

print(os.getenv('OPENAI_API_KEY'))

def reset_env():    
    os.environ.pop('OPENAI_API_KEY')
reset_env()
