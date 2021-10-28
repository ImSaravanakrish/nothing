from telethon import TelegramClient
from config import *
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


tbot = TelegramClient('botto', APP_KEY, API_HASH).start(bot_token=TOKEN)
