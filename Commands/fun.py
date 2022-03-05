import discord
import random
import asyncio
from discord.ext import commands


def setup(bot):
    bot.add_cog(funCog(bot))


class funCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def GenerateRace(self, ctx):
        await asyncio.sleep(1)
        race = ["Fairy", "Beastman", "Elve", "Dark Elve", "Demon"]
        a = random.randint(0, 100)
        if 0 <= a <= 65:
            race = "Human"
        elif 65 < a <= 90:
            race = random.choice(race)
        elif 90 < a <= 100:
            race = "God"
        else:
            return
        embed = discord.Embed(title="Race Generator !", description=f"The primordials grant you a race !",
                              color=0x00dd00)
        embed.set_thumbnail(url="https://i.ibb.co/cCgr99w/primordials-sword.png")
        embed.add_field(name="Your Race !", value=race, inline=False)
        await ctx.send(embed=embed)
