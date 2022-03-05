import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(infoCog(bot))


class infoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def Trello(self, ctx):
        embed = discord.Embed(title="Trello !", description=f"The Primordials accepts your request and gives you access to the Trello !", color=0x0079bf)
        embed.set_thumbnail(url="https://emojis.slackmojis.com/emojis/images/1450448407/160/trello.png?1450448407")
        embed.add_field(name="Discord Bot Trello", value="https://trello.com/b/M8q5hjRJ", inline=False)
        embed.add_field(name="Enarcia Mod Trello", value="https://trello.com/b/DHwBpToU", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def Tester(self, ctx):
        embed = discord.Embed(title="Become a tester !", description="The primordial grants you the right to test the bot !", color=0x5865F2)
        embed.set_thumbnail(url="https://emoji.discord.st/emojis/f08361be-6297-4c01-9ac9-92640c709e53.png")
        embed.add_field(name="Discord", value="https://discord.gg/v8CP6ukz4e", inline=False)
        await ctx.send(embed=embed)