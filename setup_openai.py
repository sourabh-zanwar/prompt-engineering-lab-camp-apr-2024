import os
from dotenv import dotenv_values

def set_env():
    #os.environ["OPENAI_API_KEY"] = dotenv_values(".env")['LLM_KEY']
    os.environ["AZURE_OPENAI_ENDPOINT"] = dotenv_values(".env")['AZURE_OPENAI_ENDPOINT']
    os.environ["AZURE_OPENAI_KEY"] = dotenv_values(".env")['AZURE_OPENAI_API_KEY']

def reset_env():    
    #os.environ.pop('OPENAI_API_KEY')
    os.environ.pop('AZURE_OPENAI_ENDPOINT')
    os.environ.pop('AZURE_OPENAI_API_KEY')
