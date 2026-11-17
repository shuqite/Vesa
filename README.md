### Hey. It's Shuqi! And there is my project - Project Vesa.

## About Vesa
Vesa is Discord bot, that uses local LLMs to chat and talk with you

## Installation guide
1. Copy .env.example to .env and fill it with your parameters
2. ```bash
   ollama serve 
   ollama pull picked_model_here
   docker compose build
   docker compose up (-d optionally)
   ```

### Dependencies:
- Docker Compose
- Ollama
- Discord bot API


## Versions:
* 0.1 - just chatting w/out context (images working) and docker compose
* 0.3 - voice chats (tts response to chat message)
* 0.5 - voice chats (tts + stt) w/out context
* 0.x - chatting (mb voice too) with context
* 1.0 - vtube model
* 1.x - adding some random funny stuff
