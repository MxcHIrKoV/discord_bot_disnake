import disnake
from disnake.ext import commands


class Events(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Бот готов к работе")

    # @commands.Cog.listener()
    # async def on_message(self, inter):
    #     # channel = self.bot.get_channel(1112709357654790205)
    #     print(inter)
    #     # print(inter.guild.name) название сервера
    #     print(inter.author.name)
    #     # await channel.send(inter.author.mention) пинг
    #     await self.bot.get_channel(1112709357654790205).send(inter.author.mention)

    @commands.Cog.listener()
    async def on_guild_join(self, inter):
        embed = disnake.Embed(
            title=f"Здарова,{inter.author.mention} на сервере {inter.guild.name}",
            description=f"Хз что тут писать, но что-то должно быть",
            color=disnake.Color.green()

        )
        await inter.send(embed=embed)
        role = inter.guild.get_role(1174676470245900368)
        await inter.user.add_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, inter):
        role = inter.guild.get_role(1174676470245900368)
        await inter.user.add_roles(role)
        await inter.send("on_member_join")


def setup(bot):
    bot.add_cog(Events(bot))
    print(f">Extension {__name__} is ready")
