import os
from typing import Annotated

from fastapi import Depends
from openai import OpenAI


def get_open_ai_client() -> OpenAI:
    client = OpenAI(
        api_key=os.getenv("BOTHUB_API_KEY"),
        base_url="https://bothub.chat/api/v2/openai/v1",
    )
    return client


open_ai_client_dep = Annotated[OpenAI, Depends(get_open_ai_client)]
