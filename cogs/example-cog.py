from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        return await ctx.send("Hello!")
def setup(bot):
    bot.add_cog(ExampleCog(bot))