import discord
from discord.ext import commands
from database.database_handler import DatabaseHandler

intents = discord.Intents().default()
intents.members = True
bot = commands.Bot(command_prefix="ù", description="Enarcia bot", intents=intents)
database_handler = DatabaseHandler("database_enarcia.db")
