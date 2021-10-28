from telethon import TelegramClient
from telethon.sessions import StringSession
import time
import os, logging
from logging import basicConfig, getLogger, INFO
"""Dasha"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()

TOKEN = os.environ.get("TOKEN")
API_KEY = os.environ.get("API_KEY")
API_HASH = os.environ.get("API_HASH")

tbot = TelegramClient(None, API_KEY, API_HASH)
