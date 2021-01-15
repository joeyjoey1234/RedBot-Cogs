import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
from .meme import MemeGen



def setup(bot):
    bot.add_cog(MemeGen(bot))
