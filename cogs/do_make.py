#Start
import discord
from discord.ext import commands
import random
my_id=339660347499872256
iljin_id=441929337562988584

answers=["OFC SENPAI!","Sure thing dude...","Yes","Okay","Sounds good","Maybe","I will try","Idk","Maybe no?","No","Definelly no","Nein","NO I SAID!"]
class Do_make(commands.Cog):
    def __init__(self, client):
        self.client=client
        
    @commands.command(aliases=["do","Do"])
    async def do_cmd(self,ctx,*,job):
        answer=random.choice(answers)
        await ctx.send(answer)

    @commands.command(aliases=["Make","make"])
    async def make_cmd(self,ctx,*,job):
        answer=random.choice(answers)
        await ctx.send(answer)

def setup(client):
    client.add_cog(Do_make(client))
#End