from src.config import settings
from ollama import AsyncClient
import logging
from typing import Any, Dict, List, Optional

from src.translator import Translate_prompt, Translate_response

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("LLM")

class Ollama_Client:
    def __init__(self) -> None:
        self.vesa_model = settings.ollama.model
        self.vesa_prompt = settings.ollama.llm_prompt
        self.client = AsyncClient(host=settings.ollama.url)

    async def generate_response(self, msg:Dict[str,str]) -> str:
        logger.info(f"prompt: {self.vesa_prompt} model: {self.vesa_model}")

        try:
            response = await self.client.chat(
                model=self.vesa_model,
                messages = [
                    {"role":"system","content":self.vesa_prompt},
                    msg
                ]
            )
            result: str = str(response.message.content)
            if settings.translator.status == True:
                result = await Translate_response(result)
            return result
        except Exception as e:
            logger.error(f"OLLAMA ERROR: {e}")
            return "Something broken in Ollama. Check logs"
