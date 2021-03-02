from os import environ, listdir
from discord import Intents
from discord.ext import commands
from difflib import get_close_matches

__import__("dotenv").load_dotenv()

bot = commands.Bot(command_prefix="py/", case_insensitive=True, intents=Intents.all(), status=discord.Status.idle, activity=discord.Game("with python"))

for cog in filter(lambda c: c.endswith(".py"), listdir("cogs/")):
    bot.load_extension(f"cogs.{cog[:-3]}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        cmd = ctx.invoked_with
        cmds = [cmd.name for cmd in bot.commands if not cmd.hidden]
        matches = get_close_matches(cmd, cmds)
        if len(matches) > 0:
            await ctx.send(f'Command "{cmd}" not found, maybe you meant "{matches[0]}"?')
        else:
            await ctx.send(f'Command "{cmd}" not found, use the help command to know what commands are available')

#Added by Running Child
#Start
admins_list=[662334026098409480]
@bot.command(aliases=["load"])
async def load_cmd(ctx, extension):
    if ctx.message.author.id in admins_list:
        try:
            bot.load_extension(f'cogs.{extension.lower()}')
            await ctx.send(extension + ' loaded.')
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")

@bot.command(aliases=["unload"])
async def unload_cmd(ctx, extension):
    if ctx.message.author.id in admins_list:
        try:
            bot.unload_extension(f'cogs.{extension.lower()}')
            await ctx.send(extension+' unloaded. Feel free to edit this! =]')
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")


@bot.command(aliases=["reload"])
async def reload_cmd(ctx,cog):
    if ctx.message.author.id in admins_list:
        try:
            bot.unload_extension(f'cogs.{cog.lower()}')
            bot.load_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"Reload of {cog.lower()} done.")
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")

#End


bot.run(environ["TOKEN"])
