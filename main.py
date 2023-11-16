import disnake
from disnake.ext import commands

from token import TOKEN

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} заробил!")
