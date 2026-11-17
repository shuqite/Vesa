import disnake
from disnake.ext import commands
import logging
from src.config import settings
from src.ollama_client import Ollama_Client
from src.translator import Translate_prompt

ollama_client = Ollama_Client()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("vesa")

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="v!", intents=intents)

@bot.command()
async def my_name_is(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.name
    await ctx.reply(f"ur name is {user_name} and id {user_id}")

@bot.command()
async def reply_image(ctx):
    images = [
        att for att in ctx.message.attachments
        if att.content_type and att.content_type.startswith("image/")
    ]
    try: image = images[0]
    except IndexError: image=0
    if image != 0:
        await image.save(f"Images/{image.filename}")
        img_path=f"Images/{image.filename}"
        img_file = disnake.File(img_path,filename=image.filename)
        await ctx.reply(file=img_file)
    else: return ctx.reply("No image attached")

async def get_image(ctx):
    images = [
        att for att in ctx.message.attachments
        if att.content_type and att.content_type.startswith("image/")
    ]
    try: image = images[0]
    except IndexError: image=None
    if image != None:
        await image.save(f"Images/{image.filename}")
        img_path=f"Images/{image.filename}"
        return img_path
    else: return image

@bot.command()
async def chat(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.display_name
    user_text = ctx.message.content[7::]
    user_image = await get_image(ctx)
    logger.info(user_image)
    if settings.translator.status == True:
        user_text = await Translate_prompt(user_text)
    prompt = f"You are talking with {user_name}. Message: {user_text}"
    message = {
        "role":"user",
        "content":prompt,
        "images": [user_image] if user_image else None
    }

    response = await ollama_client.generate_response(message)
    await ctx.reply(response)

if __name__ == "__main__":
    bot.run(settings.discord.token)
