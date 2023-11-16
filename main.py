import disnake
from disnake.ext import commands

from conf import token

bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.event
async def on_ready():
    print(f"{bot.user} заробил!")


@bot.event
async def on_

bot.run(token)
