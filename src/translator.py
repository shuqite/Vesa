import logging
from asyncio import to_thread

from deep_translator import LibreTranslator

from src.config import settings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)


__prompt_translator = LibreTranslator(
    custom_url=f"{settings.translator.url}",
    api_key="dummy",
    source="auto",
    target="en"
)
__response_translator = LibreTranslator(
    custom_url=f"{settings.translator.url}",
    api_key="dummy",
    source="en",
    target=settings.translator.language
)

async def translate_prompt(prompt: str) -> str:
    translated = await to_thread(
        __prompt_translator.translate, prompt
    )
    logger.info(f"Translated prompt: {translated}")
    return translated

async def translate_response(response: str) -> str:
    translated = await to_thread(
        __response_translator.translate, response
    )
    logger.info(f"response: {response}, translated response: {translated}")
    return translated
