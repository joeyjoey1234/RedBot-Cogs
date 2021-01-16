import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
from .meme import ImgGen



def setup(bot):
    bot.add_cog(ImgGen(bot))
