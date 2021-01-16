import subprocess
import sys
import pkg_resources


required = ['requests']
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])

from .ImgGen import ImgGen



def setup(bot):
    bot.add_cog(ImgGen(bot))
