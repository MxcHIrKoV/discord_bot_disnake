import disnake
from disnake.ext import commands


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Выводит список команд")
    async def help(self, inter):
        msg = "Здравствуйте, Вы приписали команду /help"
        await inter.response.send_message(msg)

    @commands.slash_command()
    async def server(self, inter):
        await inter.response.send_message(
            f"Название сервера: {inter.guild.name}\n Участников: {inter.guild.member_count}")

    @commands.slash_command(description="test")
    async def testembed(self, inter):
        embed = disnake.Embed(title="title", description="description", url="https://ya.ru/",
                              color=disnake.Color.green())
        embed.add_field(name="name1", value="value1", inline=True)  # доп колонки
        embed.add_field(name="name2", value="value2", inline=False)
        embed.add_field(name="name3", value="value3", inline=True)
        embed.add_field(name="name4", value="value4", inline=True)
        embed.set_image(
            url="https://avatars.mds.yandex.net/i?id=c7537a4b9d940917ffeafa165602da4f45e53645-10906089-images-thumbs&n=13")  # картинка url
        embed.set_author(name="Max", url="https://ya.ru/",
                         icon_url="https://avatars.mds.yandex.net/i?id=e56cd37df62dadba29b136d03a762b0ce233b136-9873353-images-thumbs&n=13")  # кто указыват вверху
        embed.set_footer(text=inter.author.name)  # ник внизу
        await inter.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SlashCommands(bot))
    print(f">Extension {__name__} is ready")
