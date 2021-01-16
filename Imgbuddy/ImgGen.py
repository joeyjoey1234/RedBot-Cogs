# Joejoes Cheap Meme bot

import discord
from redbot.core import commands
from random import randint
from random import choice as rnd
import requests
import json

BaseCog = getattr(commands, "Cog", object)

__version__ = "1.0"
__author__ = "Joejoe1234"

#### I really could make this function better and a ALOT SHORTER
## i was only expecting like 2 sources, but things got out of hand.
def request(reddit):
    grab = json.loads(requests.get('https://meme-api.herokuapp.com/gimme/{}'.format(reddit)).text)
    return grab['url']

def Grab_a_meme():
    memes =''
    reddits = ['','meirl', 'memes','dogelore']
    rand = randint(0,3)
    memes = request(reddits[rand])
    return memes

def Grab_a_cute():
    cutes = ''
    reddits = ['cats','awwwtf']
    rand = randint(0,1)
    cutes = request(reddits[rand])
    return cutes

def Grab_a_pat():
    pats = ''
    reddits = ['headpats']
    pats = request(reddits[0])
    return pats

patmsgs = [
    "**{user}** got a pat from **{author}**",
    "**{author}** aggressively pats **{user}**",
    " **{author}** unleashes hand pats **{user}** mmm you like that?",
    "Mmmmmmmmm you like that? **{user}**",
    "Take all my wub Owo **{user}**",
    "You deserve it **{user}**"
]

failpat = [
    "{author} Need to @ a user"
]

mememsgs = [
    "Here is a Spicy MEATBALL **{author}**",
    "Oh Daddy check this out **{author}**",
    "Suck on this bby, **{author}**",
    "Gimmie kissy **{author}**"
]


class ImgGen(BaseCog):
    """Rando Memes"""

    def __init__(self, bot):
        self.version = __version__
        self.author = __author__
        self.failpat = failpat


    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def meme(self, ctx):
        """Post rando Memes."""
        author = ctx.author

        message = rnd(mememsgs)
        meme = discord.Embed(description=message.format(author=author.name), color=discord.Color(0xffb6c1))
        meme.set_image(url=Grab_a_meme())
        await ctx.send(embed=meme)

    @commands.command()
    async def memebot_version(self, ctx):
        """Show version"""
        ver = self.version
        await ctx.send("You are using memebot version {}".format(ver))

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def cute(self, ctx):
        """Post rando cats"""
        author = ctx.author

        message = rnd(mememsgs)
        cute = discord.Embed(description=message.format(author=author.name), color=discord.Color(0xffb6c1))
        cute.set_image(url=Grab_a_cute())
        await ctx.send(embed=cute)

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def pat(self, ctx, *, user: discord.Member = None):
        """Pat users."""
        author = ctx.author

        if not user:
            message = rnd(self.failpat)
            await ctx.send(message.format(author=author.name))
        else:
            message = rnd(patmsgs)
            pat = discord.Embed(description=message.format(user=user.name, author=author.name),
                                color=discord.Color(0xffb6c1))
            pat.set_image(url=Grab_a_pat())
            await ctx.send(embed=pat)
