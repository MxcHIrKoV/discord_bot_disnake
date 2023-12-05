import disnake
from disnake.ext import commands

from conf import token

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(),
                   activity=disnake.Game("PyCharm", status=disnake.Status.offline))

bot.remove_command("help")

bot.load_extension("cogs.slash_commands")
bot.load_extension("cogs.events")


bot.run(token=token)
