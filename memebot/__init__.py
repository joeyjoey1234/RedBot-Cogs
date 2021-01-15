from .meme import MemeGen
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])


def setup(bot):
    bot.add_cog(MemeGen(bot))
