import logging

from ollama import AsyncClient

from src.config import settings
from src.role.role import pick_role
from src.translator import translate_response

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("LLM")

class OllamaClient:
    def __init__(self) -> None:
        self.vesa_model = settings.ollama.model
        self.vesa_role = pick_role(role=settings.ollama.llm_prompt)
        self.client = AsyncClient(host=settings.ollama.url)

    async def generate_response(self, msg:dict, think:bool, translate:bool) -> str:
        logger.info(f"role: {self.vesa_role} model: {self.vesa_model}")

        try:
            response = await self.client.chat(
                model=self.vesa_model,
                messages = [
                    {"role":"system","content":self.vesa_role},
                    msg
                ],
                think = think
            )
            result: str = str(response.message.content)
            if translate == True:
                result = await translate_response(result)
            return result
        except Exception as e:
            logger.error(f"OLLAMA ERROR: {e}")
            return "Something broken in Ollama. Check logs"
