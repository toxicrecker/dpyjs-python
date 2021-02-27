#Start

import discord
from discord.ext import commands
import json
import aiohttp
import random
class Memeclass(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["meme","Meme"])
    async def meme_cmd(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes.json') as r:
                res = await r.json()
                x=random.randint(0, len(res))
                data=res['data']['children'][x]['data']
                title=data['title']
                hyperlink=f"https://reddit.com{data['permalink']}"
                img_url=data['url_overridden_by_dest']
                embed_obj=discord.Embed(colour=discord.Colour.red(),url=hyperlink)
                embed_obj.title=title
                embed_obj.set_image(url=img_url)
                await ctx.send(embed=embed_obj)

    @commands.command(aliases=["animeme","Animeme"])
    async def animeme_cmd(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/animemes.json') as r:
                res = await r.json()
                x=random.randint(0, len(res))
                data=res['data']['children'][x]['data']
                title=data['title']
                hyperlink=f"https://reddit.com{data['permalink']}"
                img_url=data['url_overridden_by_dest']
                embed_obj=discord.Embed(colour=discord.Colour.red(),url=hyperlink)
                embed_obj.title=title
                embed_obj.set_image(url=img_url)
                await ctx.send(embed=embed_obj)
    
    @commands.command(aliases=["cursed","Cursed"])
    async def cursed_cmd(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/cursedcursedcomments.json') as r:
                res = await r.json()
                x=random.randint(0, len(res))
                data=res['data']['children'][x]['data']
                title=data['title']
                hyperlink=f"https://reddit.com{data['permalink']}"
                img_url=data['url_overridden_by_dest']
                embed_obj=discord.Embed(colour=discord.Colour.red(),url=hyperlink)
                embed_obj.title=title
                embed_obj.set_image(url=img_url)
                await ctx.send(embed=embed_obj)
def setup(client):
    client.add_cog(Memeclass(client))
#End