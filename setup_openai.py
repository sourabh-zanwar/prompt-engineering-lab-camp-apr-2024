import os
from access_points import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY
def set_env():
    #os.environ["OPENAI_API_KEY"] = dotenv_values(".env")['LLM_KEY']
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
    os.environ["AZURE_OPENAI_KEY"] = AZURE_OPENAI_API_KEY

def reset_env():    
    #os.environ.pop('OPENAI_API_KEY')
    os.environ.pop('AZURE_OPENAI_ENDPOINT')
    os.environ.pop('AZURE_OPENAI_API_KEY')
