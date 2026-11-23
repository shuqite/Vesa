
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
    think: bool = os.getenv("THINK","").lower() in ("yes","y","true")

@dataclass(frozen=True)
class TranslateConfig:
    status: bool = os.getenv("TRANSLATE","").lower() in ("yes","y","true")
    language: str = os.getenv("TARGET_LANG","")
    url: str = os.getenv("LIBRE_TRANSLATE_URL","")

@dataclass(frozen=True)
class Config:
    discord: DiscordConfig = DiscordConfig()
    ollama: OllamaConfig = OllamaConfig()
    translator: TranslateConfig = TranslateConfig()

settings = Config()
