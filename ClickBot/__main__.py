# By < @xditya >
# // @BotzHub //

import glob
from pathlib import Path
from ClickBot.utils import load_plugins
import logging
from . import Bot
import os
import time
import pip
import importlib
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



        

path = "ClickBot/plugins/*.py"
files = glob.glob(path)
print("\n")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        if plugin_name != "bot":
            print("\033[1;34mImporting "+plugin_name+"...")
            load_plugins(plugin_name.replace(".py", ""))
            print("\033[1;34mImported "+plugin_name+"...")

print("\033[1;34mBot Successfully deployed!")
print("\033[1;34mEnjoy!!")
banner = """\033[1;35m

      ___                       ___           ___                               
     /__/\        ___          /__/|         /__/\        ___                   
     \  \:\      /  /\        |  |:|         \  \:\      /  /\                  
      \  \:\    /  /:/        |  |:|          \__\:\    /  /:/      ___     ___ 
  _____\__\:\  /__/::\      __|  |:|      ___ /  /::\  /__/::\     /__/\   /  /\
                                   /__/::::::::\ \__\/\:\__  /__/\_|:|____ /__/\  /:/\:\ \__\/\:\__  \  \:\ /  /:/
 \  \:\~~\~~\/    \  \:\/\ \  \:\/:::::/ \  \:\/:/__\/    \  \:\/\  \  \:\  /:/ 
  \  \:\  ~~~      \__\::/  \  \::/~~~~   \  \::/          \__\::/   \  \:\/:/  
   \  \:\          /__/:/    \  \:\        \  \:\          /__/:/     \  \::/   
    \  \:\         \__\/      \  \:\        \  \:\         \__\/       \__\/    
     \__\/                     \__\/         \__\/                              
                                                   
\033[1;34mTelegram \033[1;31m: \033[1;34m@PythonEarn"""
print(banner)


if __name__ == "__main__":
    Bot.run_until_disconnected()
