# By < @xditya >
# // @BotzHub //
from .. import *
from telethon import events, Button
from subprocess import Popen, PIPE
import os
from . import bot
@Bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):

    await event.reply("Hello!",
                    buttons=KeyBoard)

@Bot.on(events.callbackquery.CallbackQuery(data="start"))
async def ex(event):
    msg = await Bot.send_message(event.chat_id,"Starting Script...")
    await bot.main(event,Bot,STRING_HASH,APP_ID,API_HASH)

    