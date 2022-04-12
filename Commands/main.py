import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="ù", description="Enarcia bot")

bot.remove_command('help')


@bot.event
async def on_ready():
    print("Ready !")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing **permissions** !")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not **found** !")
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send("Extension already **loaded** !")
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send("Extension not **loaded** !")
    else:
        await ctx.send(error)


def owner(ctx):
    return ctx.author.id == 693761548048531509


@bot.command()
@commands.check(owner)
async def load(ctx, name = None):
    if not name:
        ctx.send("Please enter a name !")
    if name:
        bot.load_extension(name)
        await ctx.send("The " + "**" + name + "**" + " file has been loaded !")


@bot.command()
@commands.check(owner)
async def unload(ctx, name = None):
    if not name:
        ctx.send("Please enter a name !")
    if name:
        bot.unload_extension(name)
        await ctx.send("The " + "**" + name + "**" + " file has been unloaded !")


@bot.command()
@commands.check(owner)
async def reload(ctx, name = None):
    if not name:
        ctx.send("Please enter a name !")
    if name:
        try:
            bot.reload_extension(name)
            await ctx.send("The " + "**" + name + "**" + " file has been reloaded !")
        except:
            bot.load_extension(name)
            await ctx.send("The " + "**" + name + "**" + " file was not loaded but I load it !")


bot.run("OTA4OTc4NDc2NjE3NDY1ODc2.YY9mLA.Uuj1sCJ3s0JcRfvNn0lg0mHaLLE")
