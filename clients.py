import os
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()


# load env 

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL_NAME")




az_client = OpenAIChatClient(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    model= AZURE_OPENAI_MODEL_NAME,
    # api_version=AZURE_OPENAI_API_VERSION
)
