from BD import tbot
from telethon.sync import events

@tbot.on(events.NewMessage(incoming=True))
async def x(e):
 if e.chat.id ==1686303934:
  try:
    for x in [-1001176306346, -1001443691244]:
        await e.forward_to(x)
  except Exception as f:
        await event.reply(f'Error {f}')
