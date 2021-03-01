#Start
import discord
from discord.ext import commands
from time import sleep
import os
from os import system, name

admins_list=[662334026098409480,339660347499872256,286591003794604034]
class Appearance(commands.Cog):

	def __init__(self, client):
		self.client = client
	@commands.command(aliases=["status"])
	async def status_cmd(self, ctx, *, activity):
		if ctx.message.author.id in admins_list:
			await self.client.change_presence(status=discord.Status.online , activity=discord.Game(activity))
			with open('./cogs/statuses.txt', 'r+') as statuses:
				statuses.truncate(0)
				statuses.write(activity)
			await ctx.send("Status successfully changed.")
		else:
			await ctx.send('U are not my master.')

	@status_cmd.error
	async def status_cmd_error(ctx,error):
		 if isinstance(error, commands.errors.MissingRequiredArgument):
			 with open('./cogs/statuses.txt', 'r') as statuses:
				 await ctx.send(statuses.read())


def setup(client):
	client.add_cog(Appearance(client))
#End