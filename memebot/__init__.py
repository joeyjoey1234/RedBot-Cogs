from .meme import MemeGen


def setup(bot):
    bot.add_cog(MemeGen(bot))
