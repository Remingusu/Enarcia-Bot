import discord
import datetime
from discord.ext import commands, tasks
from database.database_handler import DatabaseHandler

intents = discord.Intents().default()
intents.members = True
bot = commands.Bot(command_prefix="ù", description="Enarcia bot", intents=intents)
database_handler = DatabaseHandler("database_enarcia.db")


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Prisoner":
            return role
    await ctx.send("There is no role ! Create the role \"Prisoner\" please !")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def tempMute(ctx, member: discord.member, seconds: int, *, reason="Mute user"):
    mutedRole = await getMutedRole(ctx)
    database_handler.set_tempMute(member.id, ctx.guild.id, datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds))
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=f"{member} is mute for {seconds}")


@tasks.loop(seconds=1)
async def verif_unmute():
    eaa_guild = bot.get_guild(909488799485149235)
    channel = eaa_guild.get_channel(949943253623517194)
    for guild in bot.guilds:
        active = database_handler.verif_tempMute(guild.id)
        if len(active) > 0:
            mutedRole = await getMutedRole(guild)
            for row in active:
                member = guild.get_member(row["user_id"])
                database_handler.revoke_tempMute(row["id"])
                await member.remove_roles(mutedRole)
                await channel.send(f"{member}'s mute is over !")
