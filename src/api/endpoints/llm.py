from fastapi import APIRouter
from openai.types.chat import ChatCompletionUserMessageParam

from src.schemas.llm import Prompt
from src.dependencies.llm import open_ai_client_dep
from src.llm.service import get_answer_from_llm

router = APIRouter()


@router.post("/llm")
async def llm(prompt: Prompt, client: open_ai_client_dep):
    return get_answer_from_llm(client, prompt.message)
