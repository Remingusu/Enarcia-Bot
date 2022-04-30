import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.utils.manage_components import *

bot = commands.Bot(command_prefix="ù", description="Enarcia bot")
slash = SlashCommand(bot, sync_commands=True)

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
        print(error)
        await ctx.send(error)


def owner(ctx):
    return ctx.author.id == 693761548048531509


@commands.check(owner)
@slash.slash(name="Load",
             description="Load an specific extension or all",
             options=[create_option(name="extension", description="Select the extension", option_type=3, required=True,
                                    choices=[
                                          create_choice(name="Admin", value="admin"),
                                          create_choice(name="Fun", value="fun"),
                                          create_choice(name="Help", value="help"),
                                          create_choice(name="Info", value="info"),
                                          create_choice(name="All", value="all")])])
async def load(ctx, extension):
    if extension == "all":
        bot.load_extension("admin")
        bot.load_extension("fun")
        bot.load_extension("help")
        bot.load_extension("info")
        await ctx.send("All extensions have been loaded")
    else:
        bot.load_extension(extension)
        await ctx.send("The " + "**" + extension + "**" + " file has been loaded !")


@commands.check(owner)
@slash.slash(name="Unload",
             description="Unload an specific extension or all",
             options=[create_option(name="extension", description="Select the extension", option_type=3, required=True,
                                    choices=[
                                          create_choice(name="Admin", value="admin"),
                                          create_choice(name="Fun", value="fun"),
                                          create_choice(name="Help", value="help"),
                                          create_choice(name="Info", value="info"),
                                          create_choice(name="All", value="all")])])
async def unload(ctx, extension):
    if extension == "all":
        bot.unload_extension("admin")
        bot.unload_extension("fun")
        bot.unload_extension("help")
        bot.unload_extension("info")
        await ctx.send("All extensions have been unloaded")
    else:
        bot.unload_extension(extension)
        await ctx.send("The " + "**" + extension + "**" + " file has been unloaded !")


@commands.check(owner)
@slash.slash(name="Reload",
             description="Reload an specific extension or all",
             options=[create_option(name="extension", description="Select the extension", option_type=3, required=True,
                                    choices=[
                                          create_choice(name="Admin", value="admin"),
                                          create_choice(name="Fun", value="fun"),
                                          create_choice(name="Help", value="help"),
                                          create_choice(name="Info", value="info"),
                                          create_choice(name="All", value="all")])])
async def reload(ctx, extension):
    if extension == "all":
        bot.reload_extension("admin")
        bot.reload_extension("fun")
        bot.reload_extension("help")
        bot.reload_extension("info")
        await ctx.send("All extensions have been reloaded")
    else:
        bot.load_extension(extension)
        await ctx.send("The " + "**" + extension + "**" + " file has been reloaded !")


bot.run("OTA4OTc4NDc2NjE3NDY1ODc2.YY9mLA.Uuj1sCJ3s0JcRfvNn0lg0mHaLLE")
