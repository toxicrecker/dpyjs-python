#Start
import discord
from discord.ext import commands
import aiohttp
import math
import datetime

#API:8cc26d81bf2e174deea7b8d8a504279c07ba9998

class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(aliases=["osu","Osu","osuinfo","Osuinfo","OsuInfo"])
	async def osu_cmd(self, ctx,option,user,mode="standart"):
		if option.lower()=="user":
			if mode.lower()=="standart":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user?u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							embed=embed=discord.Embed(color=discord.Color.green())
							embed.title=f":flag_{res[0]['country'].lower()}: {res[0]['username']}"
							embed.set_thumbnail(url=f"http://s.ppy.sh/a/{res[0]['user_id']}")
							embed.add_field(name="Joined at:",value=f"{res[0]['join_date']}")
							embed.add_field(name="User ID", value=res[0]["user_id"], inline=False)
							embed.add_field(name="Games played:",value=f"{res[0]['playcount']}")
							embed.add_field(name="Accuracy:",value=f"{round(float(res[0]['accuracy']),2)}%")
							embed.add_field(name="Performance Points:",value=f"{round(float(res[0]['pp_raw']))}(#{int(res[0]['pp_rank']):,})")
							embed.add_field(name="Level:",value=round(float(res[0]['level']),2))
							embed.add_field(name="Total gameplay time:",value=datetime.timedelta(seconds =int(res[0]['total_seconds_played'])))
							embed.add_field(name="Ranked score:",value='{:,}'.format(int(res[0]['ranked_score'])))
							embed.add_field(name="Total score:",value='{:,}'.format(int(res[0]['total_score'])))
							embed.add_field(name="Ranks:",value=f"A:{res[0]['count_rank_a']}\nS:{res[0]['count_rank_s']}\nS Silver:{res[0]['count_rank_sh']}\nSS:{res[0]['count_rank_ss']}\nSS Silver:{res[0]['count_rank_ssh']}")
						await ctx.send(embed=embed)
						cs.close()
			elif mode.lower()=="taiko":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user?m=1&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							embed=embed=discord.Embed(color=discord.Color.green())
							embed.title=f":flag_{res[0]['country'].lower()}: {res[0]['username']}"
							embed.set_thumbnail(url=f"http://s.ppy.sh/a/{res[0]['user_id']}")
							embed.add_field(name="Joined at:",value=f"{res[0]['join_date']}")
							embed.add_field(name="User ID", value=res[0]["user_id"], inline=False)
							embed.add_field(name="Games played:",value=f"{res[0]['playcount']}")
							embed.add_field(name="Accuracy:",value=f"{round(float(res[0]['accuracy']),2)}%")
							embed.add_field(name="Performance Points:",value=f"{round(float(res[0]['pp_raw']))}(#{int(res[0]['pp_rank']):,})")
							embed.add_field(name="Level:",value=round(float(res[0]['level']),2))
							embed.add_field(name="Total gameplay time:",value=datetime.timedelta(seconds =int(res[0]['total_seconds_played'])))
							embed.add_field(name="Ranked score:",value='{:,}'.format(int(res[0]['ranked_score'])))
							embed.add_field(name="Total score:",value='{:,}'.format(int(res[0]['total_score'])))
							embed.add_field(name="Ranks:",value=f"A:{res[0]['count_rank_a']}\nS:{res[0]['count_rank_s']}\nS Silver:{res[0]['count_rank_sh']}\nSS:{res[0]['count_rank_ss']}\nSS Silver:{res[0]['count_rank_ssh']}")
						await ctx.send(embed=embed)
						cs.close()
			elif mode.lower()=="mania":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user?m=3&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							embed=embed=discord.Embed(color=discord.Color.green())
							embed.title=f":flag_{res[0]['country'].lower()}: {res[0]['username']}"
							embed.set_thumbnail(url=f"http://s.ppy.sh/a/{res[0]['user_id']}")
							embed.add_field(name="Joined at:",value=f"{res[0]['join_date']}")
							embed.add_field(name="User ID", value=res[0]["user_id"], inline=False)
							embed.add_field(name="Games played:",value=f"{res[0]['playcount']}")
							embed.add_field(name="Accuracy:",value=f"{round(float(res[0]['accuracy']),2)}%")
							embed.add_field(name="Performance Points:",value=f"{round(float(res[0]['pp_raw']))}(#{int(res[0]['pp_rank']):,})")
							embed.add_field(name="Level:",value=round(float(res[0]['level']),2))
							embed.add_field(name="Total gameplay time:",value=datetime.timedelta(seconds =int(res[0]['total_seconds_played'])))
							embed.add_field(name="Ranked score:",value='{:,}'.format(int(res[0]['ranked_score'])))
							embed.add_field(name="Total score:",value='{:,}'.format(int(res[0]['total_score'])))
							embed.add_field(name="Ranks:",value=f"A:{res[0]['count_rank_a']}\nS:{res[0]['count_rank_s']}\nS Silver:{res[0]['count_rank_sh']}\nSS:{res[0]['count_rank_ss']}\nSS Silver:{res[0]['count_rank_ssh']}")
						await ctx.send(embed=embed)
						cs.close()
			elif mode.lower()=="ctb":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user?m=2&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							embed=embed=discord.Embed(color=discord.Color.green())
							embed.title=f":flag_{res[0]['country'].lower()}: {res[0]['username']}"
							embed.set_thumbnail(url=f"http://s.ppy.sh/a/{res[0]['user_id']}")
							embed.add_field(name="Joined at:",value=f"{res[0]['join_date']}")
							embed.add_field(name="User ID", value=res[0]["user_id"], inline=False)
							embed.add_field(name="Games played:",value=f"{res[0]['playcount']}")
							embed.add_field(name="Accuracy:",value=f"{round(float(res[0]['accuracy']),2)}%")
							embed.add_field(name="Performance Points:",value=f"{round(float(res[0]['pp_raw']))}(#{int(res[0]['pp_rank']):,})")
							embed.add_field(name="Level:",value=round(float(res[0]['level']),2))
							embed.add_field(name="Total gameplay time:",value=datetime.timedelta(seconds =int(res[0]['total_seconds_played'])))
							embed.add_field(name="Ranked score:",value='{:,}'.format(int(res[0]['ranked_score'])))
							embed.add_field(name="Total score:",value='{:,}'.format(int(res[0]['total_score'])))
							embed.add_field(name="Ranks:",value=f"A:{res[0]['count_rank_a']}\nS:{res[0]['count_rank_s']}\nS Silver:{res[0]['count_rank_sh']}\nSS:{res[0]['count_rank_ss']}\nSS Silver:{res[0]['count_rank_ssh']}")
						await ctx.send(embed=embed)
						cs.close()
		elif option.lower()=="recent":
			if mode.lower()=="standart":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			elif mode.lower()=="taiko":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=1&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=1&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=1&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=1&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			elif mode.lower()=="ctb":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=2&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=2&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=2&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=2&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			elif mode.lower()=="mania":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=3&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=3&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_recent?m=3&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=3&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
		elif option.lower()=="best":
			if mode.lower()=="standart":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_best?u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_best?u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			if mode.lower()=="taiko":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=1&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=1&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=1&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=1&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			if mode.lower()=="ctb":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=2&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=2&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=2&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=2&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)
			if mode.lower()=="mania":
				async with aiohttp.ClientSession() as cs:
					async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=3&u={user}&k={os.environ['OSU_TOKEN']}") as r:
						async with ctx.typing():
							res = await r.json()
							if res==[]:
								embed=embed=discord.Embed(color=discord.Color.red())
								embed.title="Not Found."
								await ctx.send(embed=embed)
							else:
								async with cs.get(f"https://osu.ppy.sh/api/get_user?m=3&u={user}&k={os.environ['OSU_TOKEN']}") as s_r:
									res_1=await s_r.json()
									user_pic_url=f"http://s.ppy.sh/a/{res_1[0]['user_id']}"
									title=f":flag_{res_1[0]['country'].lower()}: {res_1[0]['username']}"
								embed=embed=discord.Embed(color=discord.Color.purple())
								embed.title=title
								embed.set_thumbnail(url=user_pic_url)
								async with cs.get(f"https://osu.ppy.sh/api/get_user_best?m=3&u={user}&limit=10&k={os.environ['OSU_TOKEN']}") as recents:
									given_recents=await recents.json()
									x=0
									ids=[]
									for elements in given_recents:
										ids.append(given_recents[x]['beatmap_id'])
										x+=1
									titles=[]
									for id in ids:
										async with cs.get(f"https://osu.ppy.sh/api/get_beatmaps?m=3&b={id}&limit=10&k={os.environ['OSU_TOKEN']}") as beatmaps:
											given_response=await beatmaps.json()
											titles.append(given_response[0]['title'])
								x=0
								for title in titles:
									embed.add_field(name=f"#{x+1} - {title}",value=f"Rank:{given_recents[x]['rank']} - Score:{given_recents[x]['score']} - Date: {given_recents[x]['date']}",inline=False)
									x+=1
								await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Misc(client))
#End