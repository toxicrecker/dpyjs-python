import discord
from discord.ext import commands
import DiscordUtils
import re
import datetime
import math

class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.music = DiscordUtils.Music()
		self.data = {"stop": {}, "skip": {}, "volume": {}}
	@commands.command(aliases=["l", "disconnet", "dc"])
	async def leave(self, ctx):
		channel = ctx.message.author.voice.channel
		voice = ctx.voice_client
		if voice and voice.is_connected():
			if ctx.author.voice.channel == voice.channel:
				members = len([member for member in voice.channel.members if not member.bot])
				if members == 1:
					await voice.disconnect()
					await ctx.send(f"Left **{channel}**")
				else:
					await ctx.send("I will not leave the voice channel until its only me and you in it")
			else:
				await ctx.send("Join my voice channel before using that")
		else:
			await ctx.send("Don't think I am in a voice channel")
		
	@commands.command(aliases=["p", "pl"])
	async def play(self, ctx, *, song="https://youtu.be/dQw4w9WgXcQ"):
		if not ctx.voice_client:
			voice = ctx.author.voice
			if voice:
				await ctx.send(f"Joined **{voice.channel}**")
				await voice.channel.connect()
			else:
				return await ctx.send("I can't play anything without connecting to a voice channel")
		if ctx.voice_client and ctx.author.voice.channel != ctx.voice_client.channel:
			return await ctx.send("Join my voice channel to play songs")
		player = self.music.get_player(guild_id=ctx.guild.id) or self.music.create_player(ctx, ffmpeg_error_betterfix=True)
		@player.on_play
		async def on_play(ctxx, song):
			player = self.music.get_player(guild_id=ctxx.guild.id)
			if ctxx.guild.id not in self.data["volume"]:
				self.data["volume"][ctxx.guild.id] = 100
			await player.change_volume(self.data["volume"][ctxx.guild.id]/100)
			self.data["stop"][ctx.guild.id] = []
			self.data["skip"][ctx.guild.id] = []
			await ctxx.send(f"Now playing **{song.name}** | **{datetime.timedelta(seconds=song.duration)}**")
		@player.on_queue
		async def on_queue(ctxx, song):
			await ctxx.send(f"Queued **{song.name}** | **{datetime.timedelta(seconds=song.duration)}**")
		await player.queue(song, bettersearch=False if re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", song) else True)
		if not ctx.voice_client.is_playing():
			await player.play()
			
	@commands.command(aliases=["pa"])
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def pause(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before pausing")
		song = await player.pause()
		await ctx.send(f"Paused **{song.name}**")

	@pause.error
	async def pause_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"You are on cooldown, try again after {round(error.retry_after, 1)}s")

	@commands.command(aliases=["r", "rs"])
	async def resume(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before resuming")
		song = await player.resume()
		await ctx.send(f"Resumed **{song.name}**")

	@commands.command(aliases=["s", "sk"])
	async def skip(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before skipping")
		needed = len([member for member in ctx.voice_client.channel.members if not member.bot])/2
		if needed%2==0:
			needed += 1
		else:
			needed += 0.5
		needed = math.ceil(needed)
		if ctx.guild.id not in self.data["skip"]:
			self.data["skip"][ctx.guild.id] = []
		if ctx.author.id in self.data["skip"][ctx.guild.id]:
			await ctx.send("You have already voted to skip the song")
		else:
			self.data["skip"][ctx.guild.id].append(ctx.author.id)
			voted = self.data["skip"][ctx.guild.id]
			if len(self.data["skip"][ctx.guild.id]) >= needed:
				await ctx.send(f"Got {len(voted)}/{needed} votes, skipping the song now")
				self.data["skip"][ctx.guild.id] = []
				songs = await player.skip(force=True)
				await ctx.send(f"Skipped **{songs[0].name}**")
			else:
				await ctx.send(f"Got {len(voted)}/{needed} votes, need {needed-len(voted)} more votes to skip the song")
		
	@commands.command(aliases=["st"])
	async def stop(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before stopping")
		needed = len([member for member in ctx.voice_client.channel.members if not member.bot])/2
		if needed%2==0:
			needed += 1
		else:
			needed += 0.5
		needed = math.ceil(needed)
		if ctx.guild.id not in self.data["stop"]:
			self.data["stop"][ctx.guild.id] = []
		if ctx.author.id in self.data["stop"][ctx.guild.id]:
			await ctx.send("You have already voted to stop the music")
		else:
			self.data["stop"][ctx.guild.id].append(ctx.author.id)
			voted = self.data["stop"][ctx.guild.id]
			if len(self.data["stop"][ctx.guild.id]) >= needed:
				await ctx.send(f"Got {len(voted)}/{needed} votes, stopping the music now")
				self.data["stop"][ctx.guild.id] = []
				await player.stop()
				await ctx.send("Stopped the music")
			else:
				await ctx.send(f"Got {len(voted)}/{needed} votes, need {needed-len(voted)} more votes to stop the music")
	
	@commands.command(aliases=["q", "qu"])
	async def queue(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before checking the queue")
		q = []
		queue = player.current_queue()
		if len(queue) == 0:
			return await ctx.send("Nothing in the queue")
		for i, song in enumerate(queue):
			q.append(f"{i}) **{song.name}** | **{datetime.timedelta(seconds=song.duration)}**")
		q[0] += " (Now Playing)"
		await ctx.send("\n".join(q))

	@commands.command(aliases=["rm"])
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def remove(self, ctx, index=None):
		if not index:
			return await ctx.send("Also specify the song index while using the command, use 1 for next song, use 2 for next to next song and so on")
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before removing from queue")
		if index < 0 or not isinstance(index, int):
			return await ctx.send(f"I can't understand which song in the queue has {index} position")
		elif index == 0:
			return await ctx.send("Use the skip command to skip the current song")
		elif index > len(player.current_queue()):
			return await ctx.send(f"There are only {len(player.current_queue())} songs in the queue")
		song = await player.remove_from_queue(index)
		await ctx.send(f"Removed **{song.name}** from queue")

	@remove.error
	async def pause_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"You are on cooldown, try again after {round(error.retry_after, 1)}s")

	@commands.command(aliases=["lp", "repeat", "rp"])
	async def loop(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before looping")
		song = await player.toggle_song_loop()
		if song.is_looping:
			await ctx.send(f"**{song.name}** is now looping")
		else:
			await ctx.send(f"**{song.name}** is not looping anymore")

	@commands.command(name="volume", aliases=["v"])
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def volume(self, ctx, vol=None):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before changing the volume")
		if not vol:
			return await ctx.send("Also specify the volume while using the command")
		if "%" in vol:
			vol = vol.replace("%","")
		try:
			vol = float(vol)
			vol = 100 if vol > 100 else 0 if vol < 0 else vol
			if ctx.guild.id not in self.data["volume"].keys():
				self.data["volume"][ctx.guild.id] = 100
			self.data["volume"][ctx.guild.id] = vol
			await ctx.send(f"Changed volume to {vol}%")
			await player.change_volume(vol/100)
		except ValueError:
			await ctx.send("Volume should be a number like `69` or `420`")
		
	@volume.error
	async def volume_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"You are on cooldown, try again after {round(error.retry_after, 1)}s")
		
	@commands.command(aliases=["nowplaying"])
	async def np(self, ctx):
		player = self.music.get_player(guild_id=ctx.guild.id)
		if not player: return await ctx.send("Atleast play something before checking currently playing song")
		song = player.now_playing()
		await ctx.send(f"Now playing **{song.title}** at **{self.data['volume'][ctx.guild.id]}%** volume")

def setup(bot):
	bot.add_cog(Music(bot))