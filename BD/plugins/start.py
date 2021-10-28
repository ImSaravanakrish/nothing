from BD import tbot
from telethon.sync import events


@tbot.on(events.NewMessage(pattern="[/!]start"))
async def lol(event):
  await event.reply('I am alive')
