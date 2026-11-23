import logging
from re import sub

import disnake
from disnake.ext import commands

from src.config import settings
from src.ollama_client import OllamaClient
from src.translator import translate_prompt

ollama_client = OllamaClient()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("vesa")

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="v!", intents=intents)

async def get_image(ctx):
    images = [
        att for att in ctx.message.attachments
        if att.content_type and att.content_type.startswith("image/")
    ]
    try:
        image = images[0]
        image_bytes = await image.read()
    except IndexError: image_bytes = None
    return image_bytes

class Flags(commands.FlagConverter, prefix="--", delimiter=" "):
    translate: bool = commands.flag(aliases=["tr"],default=settings.translator.status)
    think: bool = commands.flag(aliases=["th"],default=settings.ollama.think)

@bot.command()
async def chat(ctx: commands.Context, *, flags: Flags):
    # content
    # user_id = ctx.author.id
    user_name = ctx.author.display_name
    user_text = sub(r"--(tr|translate|th|think)\s+\S+", "", ctx.message.content[7::]).strip()
    user_image = await get_image(ctx)
    if user_image: logger.info(f"Image is attached: {len(user_image)} bytes")
    else: logger.info("No attached images")

    # prompt generation
    if flags.translate:
        user_text = await translate_prompt(user_text)
    prompt = f"You are chatting with user whose nickname is {user_name}. Minimize mentioning nickname in your message. Message from user: {user_text}"
    message = {
        "role":"user",
        "content":prompt,
        "images": [user_image] if user_image else None
    }

    # generate response and give it out
    response = await ollama_client.generate_response(
        msg=message,
        think=flags.think,
        translate=flags.translate
    )
    await ctx.reply(response)

if __name__ == "__main__":
    bot.run(settings.discord.token)
