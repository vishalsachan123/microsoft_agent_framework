# --------SECTION 1: IMPORTS---------

import asyncio
from agent_framework import Agent
# from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
from clients import az_client


# --- SECTION 2: CONFIGURATION ---
load_dotenv()


# ---------------------Model Credential------------------------


# --- SECTION 3: AGENT DEFINITION ---
# OpenAIChatClient() with no args reads OPENAI_API_KEY + OPENAI_MODEL from env.

agent = Agent(
    client=az_client,
    name='FirstAgent',
    instructions='You are assistant agent.'
)

# --- SECTION 4: RUN & TEST ---


async def main():
    try:
        result = await agent.run(
            "hello, How are you?"
        )
        print(f"\n Agent: {result}")
    except Exception as e:
        print(e)

asyncio.run(main())
