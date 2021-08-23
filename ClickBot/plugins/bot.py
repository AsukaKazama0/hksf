import time
import webbrowser
import time 
import subprocess
import schedule 
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
import sys, atexit
from sys import argv
import subprocess
# chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# webbrowser.register("chrome", None,webbrowser.BackgroundBrowser(chrome_path))
from telethon import TelegramClient, sync, events
from telethon import events, Button

from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os
import bs4
import selenium
from telethon.sessions import StringSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
c = requests.session()
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# CHROMEDRIVER_PATH = './chromedriver'
for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m# \033[1;37m🅻🅾🅰🅳🅸🅽🅶...")
        sys.stdout.flush() 
        sleep(2)
        os.system("clear")
        break


banner = """\033[1;31m
 /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$  | $$ /$$__  $$| $$  / $$|_____ $$  /$$__  $$| $$__  $$
| $$  | $$| $$  \ $$|  $$/ $$/     /$$/ | $$  \ $$| $$  \ $$
| $$$$$$$$| $$$$$$$$ \  $$$$/     /$$/  | $$  | $$| $$$$$$$/
| $$__  $$| $$__  $$  >$$  $$    /$$/   | $$  | $$| $$__  $$
| $$  | $$| $$  | $$ /$$/\  $$  /$$/    | $$  | $$| $$  \ $$
| $$  | $$| $$  | $$| $$  \ $$ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|__/  |__/|__/  |__/|________/ \______/ |__/  |__/

\033[1;34mTelegram \033[1;31m:\033[1;34m@PythonEarn"""
async def send_message(msg,chat_id,bot):
	await bot.send_message(chat_id,msg)
if not os.path.exists("session"):
    os.makedirs("session")

def tunggu(x,Bot,chat_id):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}
async def main(event,Bot,STRING_HASH,APP_ID,APP_HASH):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    CHROMEDRIVER_PATH = os.environ.get("GOOGLE_CHROME_PATH")
    print(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
    client = TelegramClient(StringSession(STRING_HASH), str(APP_ID),APP_HASH)
    await client.connect()
    chat_id = event.chat_id
    @client.on(events.NewMessage(incoming=True))
    async def start(event):
        if(event.message.message.find("You earned") != -1 and event.chat_id == 741849360):
            await Bot.send_message(chat_id , event.message.message)
        if(event.message.message.find("Please stay on the site for at least") != -1 and event.chat_id == 741849360):
            await Bot.send_message(chat_id , event.message.message)

    myself = await client.get_me()
    os.system("clear")
    print(banner)
    m = await event.reply("Started Working...")
    try:
        channel_entity = await client.get_entity("@Litecoin_click_bot")
        channel_username = "@Litecoin_click_bot"
        for i in range(5000000):
            await client.send_message(entity=channel_entity, message="🖥 Visit sites")
            sleep(1)
            posts = await client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            if(posts.messages[0].message.find("Sorry, there are no new ads available") != -1):
                await client.send_message(entity=channel_entity, message="💰 Balance")
                driver.quit()
                sleep(5)
                posts = await client(
                    GetHistoryRequest(
                        eer=channel_entity,
                        limit=1,
                        offset_date=None,
                        offset_id=0,
                        max_id=0,
                        min_id=0,
                        add_offset=0,
                        hash=0,
                    )
                )
                message = posts.messages[0].message
                await m.edit(message)
                sys.exit()
            else:
                try:
                    url = posts.messages[0].reply_markup.rows[0].buttons[0].url

                    await Bot.send_message(chat_id,"Opening Site...")
                    driver.get(url)

                    id = posts.messages[0].id
                    

                    r = c.get(url, headers=ua, timeout=65, allow_redirects=True)
                    soup = BeautifulSoup(r.content, "html.pasrser")
                    if (
                        soup.find("div", id="headbar") is None
                    ):
                        sleep(15)
                        posts = await client(
                            GetHistoryRequest(
                                peer=channel_entity,
                                limit=1,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                            )
                        )
                        message = posts.messages[0].message
                        if (
                            posts.messages[0].message.find("You must stay") != -1
                            or posts.messages[0].message.find("Please stay on the site for at least 10 seconds...") != -1
                        ):
                            sec = re.findall(r"([\d.]*\d+)", message)

                            tunggu(int(sec[0]),Bot,chat_id)
                            sleep(1)
                            posts = await client(
                                GetHistoryRequest(
                                peer=channel_entity,
                                limit=2,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                                )
                            )
                            messageres = posts.messages[1].message
                            sleep(1)
                            await m.edit(messageres)
                        else:
                            sleep(65)
                            pass

                    elif soup.find("div", id="headbar") is not None:
                            for dat in soup.find_all("div", class_="container-fluid"):
                                code = dat.get("data-code")
                                timer = dat.get("data-timer")
                                tokena = dat.get("data-token")
                                tunggu(int(timer),Bot,chat_id)
                                r = c.post(
                                "https://dogeclick.com/reward",
                                data={"code": code, "token": tokena},
                                headers=ua,
                                timeout=15,
                                allow_redirects=True,
                            )
                            js = json.loads(r.text)
                            msg = "You earned "+ js["reward"] + " LTC for visiting a site!"
                            await Bot.send_message(chat_id,msg)
                    else:
                        msg = "Captcha Detected! Skipping..."
                        await Bot.send_message(chat_id,msg)
                        sleep(65)
                        await client(
                            GetBotCallbackAnswerRequest(
                                channel_username,
                                id,
                                data=posts.messages[0].reply_markup.rows[1].buttons[1].data,
                            )
                        )
                    
                        sleep(1)
                except:
                    sleep(1)
                    posts = await client(
                        GetHistoryRequest(
                            peer=channel_entity,
                            limit=1,
                            offset_date=None,
                            offset_id=0,
                            max_id=0,
                            min_id=0,
                            add_offset=0,
                            hash=0,
                            )
                    )
                    message = posts.messages[0].message
                    if (
                    posts.messages[0].message.find("You must stay") != -1
                    or posts.messages[0].message.find("Please stay on") != -1
                    ):
                        sec = re.findall(r"([\d.]*\d+)", message)
                        tunggu(int(sec[0]),Bot,chat_id)
                        sleep(1)
                        posts = await client(
                            GetHistoryRequest(
                                peer=channel_entity,
                                limit=2,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                            )
                        )
                        messageres = posts.messages[1].message
                        sleep(1)
                    else:
                        sleep(65)
                        pass
    finally:
        await client.disconnect()
        driver.quit()
