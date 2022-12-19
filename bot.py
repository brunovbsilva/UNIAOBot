import os
from decouple import config
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix="u!", intents=intents)

def load_cogs(bot):
    bot.load_extension("manager")
    for file in os.listdir("commands"):
        if(file.endswith(".py")):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")
    for file in os.listdir("tasks"):
        if(file.endswith(".py")):
            cog = file[:-3]
            bot.load_extension(f"tasks.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)