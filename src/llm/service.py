import logging
from os import name

from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)


def get_answer_from_llm(client: OpenAI, msg: str):
    try:
        messages: list[ChatCompletionUserMessageParam] = [
            {"role": "user", "content": msg}
        ]
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=messages,
        )
        logger.info("Запрос прошёл успешно.")
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return None
