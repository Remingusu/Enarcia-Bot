import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(helpCog(bot))


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def help(self, ctx):
        embed = discord.Embed(title="HELP !", value="Need Help ?", color=0xDEFD00)

        await ctx.send(embed=embed)