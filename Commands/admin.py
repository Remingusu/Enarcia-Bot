import discord
import random
import asyncio
from discord.ext import commands


def setup(bot):
    bot.add_cog(adminCog(bot))


class adminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *reason):
        reason = " ".join(reason)
        author = ctx.message.author
        nembed = discord.Embed(title="**BAN !**", description="**The Primordials are angry !**", color=0xcd1717)
        nembed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        nembed.add_field(name="What's going on ?", value=f"***{user}*** was *DISINTEGRATED*", inline=False)
        nembed.add_field(name="By whom ?", value=f"The primordials examined the report of {author.mention} !",
                         inline=False)
        nembed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)

        embed = discord.Embed(title="**BAN !**", description=f"**The Primordials are angry !**", color=0xcd1717)
        embed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        embed.add_field(name="What's going on ?", value=f"***{user}*** was *DISINTEGRATED*", inline=False)
        embed.add_field(name="By whom ?", value=f"The primordials examined the report of {author.mention} !",
                        inline=False)
        embed.add_field(name="The reason", value=f"{reason}", inline=False)
        embed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)
        if not reason:
            await ctx.guild.ban(user)
            await ctx.send(embed=nembed)
        else:
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempBan(self, ctx, user: discord.User, *reason):
        await ctx.send("The command is not ready !"
                       "See the Trello: https://trello.com/b/M8q5hjRJ")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user):
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user)
                await ctx.send(f"{user} was **RESUSCITATED** !")
                return
        await ctx.send(f"{user} is not among the **DEAD** !")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User, *reason):
        reason = " ".join(reason)
        author = ctx.message.author
        nembed = discord.Embed(title="**KICK !**", description=f"**The Primordials are angry !**", color=0xef9b00)
        nembed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        nembed.add_field(name="What's going on ?", value=f"***{user}*** was *KICKED* from the Village", inline=False)
        nembed.add_field(name="By whom ?", value=f"By the primordials through {author.mention} !", inline=False)
        nembed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)

        embed = discord.Embed(title="**KICK !**", description=f"**The Primordials are angry !**", color=0xef9b00)
        embed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        embed.add_field(name="What's going on ?", value=f"***{user}*** was *KICKED* from the Village", inline=False)
        embed.add_field(name="By whom ?", value=f"By the primordials through {author.mention} !", inline=False)
        embed.add_field(name="The reason", value=f"{reason}", inline=False)
        embed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)
        if not reason:
            await ctx.guild.kick(user)
            await ctx.send(embed=nembed)
        else:
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(embed=embed)

    async def getMutedRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Prisoner":
                return role
        await ctx.send("There is no role ! Create the role \"Prisoner\" please !")
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *reason):
        author = ctx.message.author
        reason = " ".join(reason)
        guild = self.bot.get_guild(751466454918103171)
        channel = guild.get_channel(922624543426752594)
        mutedRole = await self.getMutedRole(ctx)
        nembed = discord.Embed(title="**MUTE !**", description=f"**The Primordials are angry !**", color=0xc5307a)
        nembed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        nembed.add_field(name="What's going on ?", value=f"***{member.mention}*** was **IMPRISONED**", inline=False)
        nembed.add_field(name="By whom ?", value=f"By the primordials through {author.mention} !", inline=False)
        nembed.add_field(name="Info !", value="To go talk to him go into the channel #prison", inline=False)
        nembed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)

        embed = discord.Embed(title="**MUTE !**", description=f"**The Primordials are angry !**", color=0xc5307a)
        embed.set_thumbnail(url="https://i.ibb.co/2j2D7gR/angry-primordials.png")
        embed.add_field(name="What's going on ?", value=f"***{member.mention}*** was **IMPRISONED**", inline=False)
        embed.add_field(name="By whom ?", value=f"By the primordials through {author.mention} !", inline=False)
        embed.add_field(name="The reason", value=f"{reason}", inline=False)
        embed.add_field(name="Info !", value="To go talk to him go into the channel #prison", inline=False)
        embed.add_field(name="Will you click on this link ?", value="https://tinyurl.com/388zn9mn", inline=False)
        if not reason:
            await member.add_roles(mutedRole, reason="muted")
            await ctx.send(embed=nembed)
        else:
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await channel.send("Send *visit (in the #enarcia-bot) for get the visitor role and talk to the prisoner.")

    async def getVisitRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Visitor":
                return role
        await ctx.send("There is no role ! Create the role \"Visitor\" please !")
    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def visit(self, ctx):
        author = ctx.message.author
        visitRole = await self.getVisitRole(ctx)
        await author.add_roles(visitRole)
        await ctx.send("You are now a visitor...")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempMute(self, ctx):
        await ctx.send("The command is not ready !"
                       "See the Trello: https://trello.com/b/M8q5hjRJ")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = await self.getMutedRole(ctx)
        await member.remove_roles(mutedRole)
        await ctx.send(f"***{member.mention}*** **has been released from** ***PRISON*** **!**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, nbr: int):
        msgs = await ctx.channel.history(limit=nbr + 1).flatten()
        for message in msgs:
            await message.delete()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clearAll(self, ctx):
        msgs = await ctx.channel.history(limit=None).flatten()
        for message in msgs:
            await message.delete()

    async def getSlaveRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Slave":
                return role
        await ctx.send("There is no role ! Create the role \"Slave\" please !")
    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True, manage_messages=True, manage_roles=True)
    async def Judgement(self, ctx, member: discord.Member, *reason):
        reason = " ".join(reason)
        author = ctx.message.author
        if not reason:
            await ctx.send(f"**The hour of** *JUDGEMENT* **has come !** "
                           f"\n {member.mention} **will be judged because he broke a rule,"
                           f" according to** {author.mention} **.**")
        else:
            await ctx.send(f"**The hour of** *JUDGEMENT* **has come !** "
                           f"{member.mention} **will be judged because he is accused of** "
                           f"***{reason}*** **by** {author.mention} **.**")
        await asyncio.sleep(1)
        await ctx.send(f"I ask for your **silence** ! The session starts in *5 seconds* and will last *10 seconds*!")
        await asyncio.sleep(5)
        await ctx.send(f"The session start !")

        def checkSilence(message):
            return message.channel == ctx.message.channel

        try:
            while True:
                await self.bot.wait_for('message', timeout=10, check=checkSilence)
                await ctx.send("**QUIET !**\n The session lasts *10 seconds* !")
        except:
            sentence = ["Ban", "Temp Ban", "Kick", "Mute", "Slave role"]
            await ctx.send(f"After deliberation, {member.mention} will have as sentence...")
            deliberation = random.choice(sentence)
            await asyncio.sleep(3)
            await ctx.send("a " + "**" + deliberation + "**")
            await ctx.send(f"You have *1 minute* to say ***goodbye*** before you get **{deliberation}**")
        await asyncio.sleep(60)
        await ctx.send("**BYE !**")
        if deliberation == "Ban":
            await member.ban()
        elif deliberation == "Temp Ban":
            await ctx.send("Not yet")
        elif deliberation == "Kick":
            await member.kick()
        elif deliberation == "Mute":
            mutedRole = await self.getMutedRole(ctx)
            await member.add_roles(mutedRole, reason="muted")
        else:
            slaveRole = await self.getSlaveRole(ctx)
            await member.add_roles(slaveRole, reason="Judgement")
