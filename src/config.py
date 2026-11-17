import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class DiscordConfig:
    token: str = os.getenv("DISCORD_TOKEN", "")

@dataclass(frozen=True)
class OllamaConfig:
    model: str = os.getenv("LLM","")
    llm_prompt: str = os.getenv("MAIN_PROMPT","")
    url: str = os.getenv("OLLAMA_URL","")

@dataclass(frozen=True)
class TranslateConfig:
    status: bool = bool(os.getenv("TRANSLATE",""))
    language: str = os.getenv("LANG","")
    url: str = os.getenv("LIBRE_TRANSLATE_URL","")

@dataclass(frozen=True)
class Config:
    discord: DiscordConfig = DiscordConfig()
    ollama: OllamaConfig = OllamaConfig()
    translator: TranslateConfig = TranslateConfig()


settings = Config()
