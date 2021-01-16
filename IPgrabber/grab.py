# just goofin

import discord
from redbot.core import commands


BaseCog = getattr(commands, "Cog", object)

__version__ = "1.0"
__author__ = "Joejoe1234"

message = 'sup'

class grab(BaseCog):
    """Rando Memes"""

    def __init__(self, bot):
        self.version = __version__
        self.author = __author__


    @commands.command()
    async def lol(self, ctx):
        """lol maybe grab it"""
        author = ctx.author


        meme = discord.Embed(description=message, color=discord.Color(0xffb6c1))
        meme.set_image(url='http://joepena.dev/lol.png')
        await ctx.send(embed=meme)

