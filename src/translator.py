from asyncio import to_thread

from deep_translator import LibreTranslator
from src.config import settings
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)


async def Translate_prompt(prompt: str) -> str:
    translated = await to_thread(
        lambda: LibreTranslator(
            custom_url=f"{settings.translator.url}",
            api_key="dummy",
            source="auto",
            target="en").translate(prompt)
    )
    logger.info(f"Translated prompt: {translated}")
    return translated

async def Translate_response(response: str) -> str:
    lang = settings.translator.language
    translated = await to_thread(
        lambda: LibreTranslator(
            custom_url=f"{settings.translator.url}",
            api_key="dummy",
            source="en",
            target=f"{lang}").translate(response)
    )
    logger.info(f"response: {response}, translated response: {translated}")
    return translated
