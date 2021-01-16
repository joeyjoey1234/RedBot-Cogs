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

def Grab_a_meme():
    memes = []
    r1 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme/wholesomememes').text)
    r2 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme').text)
    r3 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme/technicallythetruth').text)
    memes.append(r1['url'])
    memes.append(r2['url'])
    memes.append(r3['url'])
    rand = randint(0, 2)
    return memes[rand]


Grab_a_meme()

mememsgs = [
    "Here is a Spicy MEATBALL **{author}**",
    "Oh Daddy check this out **{author}**",
    "Suck on this bby, **{author}**"
]


class MemeGen(BaseCog):
    """Rando Memes"""

    def __init__(self, bot):
        self.meme = Grab_a_meme()

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def meme(self, ctx, *, user: discord.Member=None):
        """Post rando Memes."""
        author = ctx.author

        message = rnd(mememsgs)
        meme = discord.Embed(description=message.format(author=author.name), color=discord.Color(0xffb6c1))
        meme.set_image(url=self.meme)
        await ctx.send(embed=meme)

