# Joejoes Cheap Meme bot

# Discord
import discord

# Red
from redbot.core import commands
import requests
# Libs
from random import choice as rnd
import requests
import json
BaseCog = getattr(commands, "Cog", object)

__version__ = "1.0"
__author__ = "Joejoe1234"

memes = []
r1 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme/wholesomememes').text)
r2 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme').text)
r3 = json.loads(requests.get('https://meme-api.herokuapp.com/gimme/technicallythetruth').text)
memes.append(r1['url'])
memes.append(r2['url'])
memes.append(r3['url'])




mememsgs = [
    "Here is a Spicy MEATBALL **{author}**",
    "Oh Daddy check this out **{author}**",
    "Suck on this bby, **{author}**"
]


class MemeGen(BaseCog):
    """Rando Memes"""

    def __init__(self, bot):
        self.memes = memes

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def meme(self, ctx, *, user: discord.Member=None):
        """Post rando Memes."""
        author = ctx.author

        message = rnd(mememsgs)
        meme = discord.Embed(description=message.format(author=author.name), color=discord.Color(0xffb6c1))
        meme.set_image(url=rnd(self.memes))
        await ctx.send(embed=meme)