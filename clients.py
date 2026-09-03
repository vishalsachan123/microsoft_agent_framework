from agent_framework.openai import OpenAIChatClient




# load env 



az_client = OpenAIChatClient(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    model= AZURE_OPENAI_MODEL_NAME,
    # api_version=AZURE_OPENAI_API_VERSION
)
