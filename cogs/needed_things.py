#Start
import discord
from discord.ext import commands
import datetime
import asyncio 
import typing
import aiohttp
from htmllaundry import strip_markup

class Needed_things(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command(aliases=["avatar"])
    async def avatar_cmd(self,ctx,user:discord.Member):
        async with ctx.typing():
            embed_obj=discord.Embed(colour=discord.Colour.dark_purple())
            embed_obj.title=f"{user.display_name}'s avatar"
            embed_obj.set_image(url=user.avatar_url_as())
            embed_obj.set_footer(text=f"Requested by {ctx.message.author.display_name}", icon_url=ctx.message.author.avatar_url_as())
        await ctx.send(embed=embed_obj)
            

    @avatar_cmd.error
    async def avatar_cmd_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            async with ctx.typing():
                embed_obj=discord.Embed(colour=discord.Colour.dark_purple())
                embed_obj.title=f"{ctx.message.author.display_name}'s avatar"
                embed_obj.set_image(url=ctx.message.author.avatar_url_as())
            await ctx.send(embed=embed_obj)
        else:
            raise error

    @commands.command(aliases=["userinfo"])
    async def userinfo_cmd(self,ctx,user:discord.Member):
        async with ctx.typing():
            if user.nick==None:
                user_nick=user.display_name
            elif user.nick!=None:
                user_nick=user.nick
            roles_of_user=""
            roles_of_user+="@everyone"

            for role in user.roles:
                if role.name=="@everyone":
                    roles_of_user+=""
                else:
                    roles_of_user+=role.mention

            embed_obj=discord.Embed(colour=discord.Colour.teal())
            embed_obj.title=f"{user_nick}'s info"
            embed_obj.add_field(name="Account's creation date",value=user.created_at)
            embed_obj.add_field(name="Joined this server at",value=user.joined_at)
            embed_obj.add_field(name="Roles",value=roles_of_user)
            embed_obj.set_thumbnail(url=user.avatar_url_as())
            embed_obj.add_field(name="Nick in this server:",value=user.nick)
            embed_obj.add_field(name="Name in Discord:",value=user.name)
            embed_obj.add_field(name="User ID:",value=user.id)
            embed_obj.set_footer(text=f"Requested by {ctx.message.author.display_name}", icon_url=ctx.message.author.avatar_url_as())
        await ctx.send(embed=embed_obj)

    @userinfo_cmd.error
    async def userinfo_cmd_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            async with ctx.typing():   
                if ctx.message.author.nick==None:
                    user_nick=ctx.message.author.display_name
                elif ctx.message.author.nick!=None:
                    user_nick=ctx.message.author.nick
                roles_of_user=""
                roles_of_user+="@everyone"

                for role in ctx.message.author.roles:
                    if role.name=="@everyone":
                        roles_of_user+=""
                    else:
                        roles_of_user+=role.mention

                embed_obj=discord.Embed(colour=discord.Colour.teal())
                embed_obj.title=f"{user_nick}'s info"
                embed_obj.add_field(name="Account's creation date",value=ctx.message.author.created_at)
                embed_obj.add_field(name="Joined this server at",value=ctx.message.author.joined_at)
                embed_obj.add_field(name="Roles",value=roles_of_user)
                embed_obj.set_thumbnail(url=ctx.message.author.avatar_url_as())
                embed_obj.add_field(name="Nick in this server:",value=ctx.message.author.nick)
                embed_obj.add_field(name="Name in Discord:",value=ctx.message.author.name)
                embed_obj.add_field(name="User ID:",value=ctx.message.author.id)
            await ctx.send(embed=embed_obj)
        else:
            raise error
    @commands.command(aliases=["serverinfo"])
    async def serverinfo_cmd(self,ctx):
        async with ctx.typing():
            owner=self.client.get_user(ctx.guild.owner_id)
            embed_obj=discord.Embed(colour=discord.Colour.red())
            embed_obj.title=f"{ctx.guild.name}'s info"
            embed_obj.add_field(name="Owner of server:",value=owner)
            embed_obj.add_field(name="Creation date:",value=ctx.guild.created_at.replace(microsecond=0))
            embed_obj.set_thumbnail(url=ctx.guild.icon_url)
            embed_obj.add_field(name="Region:",value=ctx.guild.region)
            embed_obj.add_field(name="Voice channels:",value=len(ctx.guild.voice_channels))
            embed_obj.add_field(name="Current number of members in server:",value=len(ctx.guild.members))
            embed_obj.add_field(name="Number of roles:",value=len(ctx.guild.roles))
            if ctx.guild.banner is not None:
                embed_obj.add_field(name="Banner of server:",value="\U0000200b")
                embed_obj.set_image(url=ctx.guild.banner_url_as())
            embed_obj.set_footer(text=f"Server ID:{ctx.guild.id}\nRequested by {ctx.message.author.display_name}", icon_url=ctx.message.author.avatar_url_as())
        await ctx.send(embed=embed_obj)


    @commands.command(aliases=["vote"])
    async def vote_cmd(self, ctx, countdown: typing.Optional[int] = 30, *,args):
        embed = discord.Embed(
            colour = discord.Colour.gold()
        )
        args_list=args.split(",")
        embed.title="Time to vote!"
        if countdown==None:
            footer=f"Countdown not presented. Default is 30 seconds."
        elif countdown!=None:
            footer=f"Countdown set to {countdown} seconds."
        embed.add_field(name=args_list[0],value="🔼 for voting to this.")
        embed.add_field(name=args_list[1],value="🔽 for voting to this.")
        embed.set_footer(text=footer)
        upvote="🔼"
        downvote="🔽"
        vote_embed_but_it_is_msg=await ctx.send(embed=embed)
        await vote_embed_but_it_is_msg.add_reaction(upvote)
        await vote_embed_but_it_is_msg.add_reaction(downvote)
        vote_embed_id=vote_embed_but_it_is_msg.id
        await asyncio.sleep(int(countdown))
        after_vote=await ctx.channel.fetch_message(vote_embed_id)
        await vote_embed_but_it_is_msg.delete()
        up=0
        down=0
        for reactions in after_vote.reactions:
            if reactions.emoji=="🔼":
                up=reactions.count - 1
            elif reactions.emoji=="🔽":
                down=reactions.count - 1
        result_embed=discord.Embed(colour=discord.Colour.gold())
        if down<up:
            decision=args_list[0]
            result_embed.title=f"Vote ended. Seems like most users voted to {decision}"
        elif down>up:
            decision=args_list[1]
            result_embed.title=f"Vote ended. Seems like most users voted to {decision}"
        elif down==up:
            decision="Seems like no one won..."
            result_embed.title=f"{decision}"
        await ctx.send(embed=result_embed)

    @vote_cmd.error
    async def vote_cmd_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage:\nPi Vote 15(optional) argument 1,argument 2(required)")
        else:
            raise error
    @commands.command(aliases=["quote"])
    async def quote_cmd(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://zenquotes.io/api/random") as r:
                res = await r.json(content_type='text/plain') 
                quote= res[0]["q"]
                author= res[0]["a"]
                embed_obj=discord.Embed(colour=discord.Colour.red())
                embed_obj.title=quote
                embed_obj.set_footer(text=f"Author:{author}")
                await ctx.send(embed=embed_obj)
    @commands.command(aliases=["anilist","aniinfo","animeinfo"])
    async def mal_cmd(self,ctx,type,*,name):
        if type.lower()=="anime":
            query = '''
            query ($id: Int, $page: Int, $perPage: Int, $search: String) {
                Page (page: $page, perPage: $perPage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                        perPage
                    }
                    media (id: $id, search: $search, type: ANIME) {
                        id
                        title {
                        romaji
                        english
                        native
                        }
                        status
                        startDate{
                        year
                        month
                        day
                        }
                        episodes
                        format
                        coverImage{
                        large
                        }
                        bannerImage
                        siteUrl
                        source
                        type
                        averageScore
                        meanScore
                        description
                    }
                }
            }
            '''
            variables = {
                'search': name,
                'page': 1,
                'perPage': 3
            }
            url = 'https://graphql.anilist.co'

            async with aiohttp.ClientSession() as session:
                async with session.post(url,json={'query':query,'variables':variables}) as response:
                    responsed=await response.json()
                    page=responsed['data']['Page']
                    media=page['media']
                    result=media[0]
                    embed_obj=discord.Embed(colour=discord.Colour.red(),url=result['siteUrl'])
                    embed_obj.set_thumbnail(url=result['coverImage']['large'])
                    embed_obj.set_image(url=result['bannerImage'])
                    if result['title']['english']=="None":
                        embed_obj.title=f"{result['title']['romaji']}({result['title']['native']})"
                    else:
                        embed_obj.title=f"{result['title']['romaji']}({result['title']['native']})"
                    embed_obj.add_field(name="Status:",value=result['status'])
                    embed_obj.add_field(name='Started at:',value=f"{result['startDate']['year']}/{result['startDate']['month']}/{result['startDate']['day']}")
                    embed_obj.add_field(name="Episodes:",value=result['episodes'])
                    embed_obj.add_field(name="Type:",value=result['type'])
                    embed_obj.add_field(name="Average score:",value=result['averageScore'])
                    embed_obj.add_field(name="Mean score:",value=result['meanScore'])
                    if len(result['description'])>1024:
                        await(ctx.send("Synopsis is more than 1024 characters.Wanna me to send synopsis here?\n*Yes/No*\n*Timeout set to 20 seconds.*"))    
                    else:
                        embed_obj.add_field(name='Synopsis:',value=strip_markup(result['description']),inline=True)
                    await ctx.send(embed=embed_obj)
                    def check(message):
                        if message.content.lower()=="yes" or message.content.lower()=="y":
                            return True
                        elif message.content.lower()=="no" or message.content.lower()=="n":
                            return False
                    await self.client.wait_for('message',timeout=20,check=check)
                    description=strip_markup(result['description'])
                    await ctx.send(description)
        if type.lower()=="manga":
            query = '''
            query ($id: Int, $page: Int, $perPage: Int, $search: String) {
                Page (page: $page, perPage: $perPage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                        perPage
                    }
                    media (id: $id, search: $search, type: MANGA) {
                        id
                        title {
                        romaji
                        english
                        native
                        }
                        status
                        startDate{
                        year
                        month
                        day
                        }
                        episodes
                        format
                        coverImage{
                        large
                        }
                        bannerImage
                        siteUrl
                        source
                        type
                        averageScore
                        meanScore
                        description
                    }
                }
            }
            '''
            variables = {
                'search': name,
                'page': 1,
                'perPage': 3
            }
            url = 'https://graphql.anilist.co'

            async with aiohttp.ClientSession() as session:
                async with session.post(url,json={'query':query,'variables':variables}) as response:
                    responsed=await response.json()
                    page=responsed['data']['Page']
                    media=page['media']
                    result=media[0]
                    embed_obj=discord.Embed(colour=discord.Colour.red(),url=result['siteUrl'])
                    embed_obj.set_thumbnail(url=result['coverImage']['large'])
                    if result['title']['english']=="None":
                        embed_obj.title=f"{result['title']['romaji']}({result['title']['native']})"
                    else:
                        embed_obj.title=f"{result['title']['romaji']}({result['title']['native']})"
                    embed_obj.add_field(name="Status:",value=result['status'])
                    embed_obj.add_field(name='Started at:',value=f"{result['startDate']['year']}/{result['startDate']['month']}/{result['startDate']['day']}")
                    embed_obj.add_field(name="Episodes:",value=result['episodes'])
                    embed_obj.add_field(name="Type:",value=result['type'])
                    embed_obj.add_field(name="Average score:",value=result['averageScore'])
                    embed_obj.add_field(name="Mean score:",value=result['meanScore'])
                    if len(result['description'])>1024:
                        await(ctx.send("Synopsis is more than 1024 characters.Wanna me to send synopsis here?\n*Yes/No*\n*Timeout set to 20 seconds.*"))    
                    else:
                        embed_obj.add_field(name='Synopsis:',value=strip_markup(result['description']),inline=True)
                    await ctx.send(embed=embed_obj)
                    def check(message):
                        if message.content.lower()=="yes" or message.content.lower()=="y":
                            return True
                        elif message.content.lower()=="no" or message.content.lower()=="n":
                            return False
                    await self.client.wait_for('message',timeout=20,check=check)
                    description=strip_markup(result['description'])
                    await ctx.send(description)
        # else:
        #     await ctx.send(f"Unknown option:`{option}`.\nUsage: `pi anilist <anime/manga> <name of anime/manga>`")

def setup(client):
    client.add_cog(Needed_things(client))
#End