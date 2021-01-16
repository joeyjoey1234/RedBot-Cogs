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
    memes = []
    reddits = ['wholesomememes','', 'technicallythetruth', 'meirl', 'memes', 'ComedyCemetery', 'terriblefacebookmemes'
        , 'nukedmemes', 'surrealmemes', 'comedyheaven', 'dogelore']
    for x in reddits:
        memes.append(request(x))
    rand = randint(0, 10)
    return memes[rand]

def Grab_a_cat():
    cats = []
    reddits = ['cats','awwwtf']
    for x in reddits:
        cats.append(request(x))
    rand = randint(0, 1)
    return cats[rand]



mememsgs = [
    "Here is a Spicy MEATBALL **{author}**",
    "Oh Daddy check this out **{author}**",
    "Suck on this bby, **{author}**",
    "Gimmie kissy **{author}**"
]


class MemeGen(BaseCog):
    """Rando Memes"""

    def __init__(self, bot):
        self.version = __version__
        self.author = __author__


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
    async def cat(self, ctx):
        """Post rando cats"""
        author = ctx.author

        message = rnd(mememsgs)
        cat = discord.Embed(description=message.format(author=author.name), color=discord.Color(0xffb6c1))
        cat.set_image(url=Grab_a_cat())
        await ctx.send(embed=cat)
