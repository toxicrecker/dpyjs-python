from discord.ext import commands
import discord
import requests
import urllib
import datetime

class Preview(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['prev'])
    async def preview(self, ctx, *, song):
      try:
        rk = requests.get(f'https://api.deezer.com/search/track/autocomplete?limit=1&q={song}')
        jk = rk.json()	
        urllib.request.urlretrieve(f'{jk["data"][0]["preview"]}', f'{jk["data"][0]["title_short"]}.mp3')
        embed = discord.Embed(description=f'Preview of `{jk["data"][0]["artist"]["name"]} - {jk["data"][0]["album"]["title"]}` `[{str(datetime.timedelta(seconds=jk["data"][0]["duration"]))}]`', colour=0x2f3136)
        embed.set_image(url=jk["data"][0]["album"]["cover_medium"])
        m = await ctx.send(embed=embed)
        await ctx.send(file=discord. File(f'{jk["data"][0]["title_short"]}.mp3'))
      except Exception as e:
        embed = discord.Embed(description=f'We were unable to find that song, try again later.', colour=0x2f3136)

        m = await ctx.send(embed=embed)
        print(e)


def setup(bot):
    bot.add_cog(Preview(bot))
