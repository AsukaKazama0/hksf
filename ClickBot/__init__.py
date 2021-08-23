# By < @xditya >
# // @BotzHub //

from telethon import TelegramClient
from decouple import config
from telethon import events, Button

import logging
import time
import os
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
STRING_HASH = config("BOT_TOKEN", default=None)
APP_ID = 7577827

Bot = TelegramClient('Bot', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 
KeyBoard = [
            [
                Button.inline("Start Script",data="start"),
                Button.inline("Stop Script",data="stop")
            ],
            [
                Button.url("Help", url="https://t.me/"),
            ]
         ]