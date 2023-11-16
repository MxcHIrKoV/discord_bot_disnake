import disnake
from disnake.ext import commands

from conf import token

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} заробил!")

@bot.event
async def on_member_join(ctx):
    embed = disnake.Embed(
        title="Новый участник",
        description=f"{ctx.name}#{ctx.discriminator}",
        color=0x00FFCD
    )
    await ctx.send(embed=embed)


@bot.slash_command()
async def server_info(inter):
    embed = disnake.Embed(
        title="Информация о сервере",
        description=f"Название сервера: {inter.guild.name}\nКоличесво участников: {inter.guild.member_count}",
        color=0x7800FF
    )
    await inter.send(embed=embed)


bot.run(token)
