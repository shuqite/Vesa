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
async def chat(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.display_name
    user_text = ctx.message.content[7::]
    if settings.translator.status == True:
        user_text = await Translate_prompt(user_text)
    prompt = f"You are talking with {user_name}. Message: {user_text}"
    message = {"role":"user", "content":prompt}

    response = await ollama_client.generate_response(message)
    await ctx.reply(response)

if __name__ == "__main__":
    bot.run(settings.discord.token)
