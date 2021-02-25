from os import environ, listdir
from discord import Intents
from discord.ext import commands

__import__("dotenv").load_dotenv()

bot = commands.Bot(command_prefix="py/", case_insensitive=True, intents=Intents.all())

for cog in filter(lambda c: c.endswith(".py"), listdir("cogs/")):
    bot.load_extension(f"cogs.{cog[:-3]}")

bot.run(environ["TOKEN"])