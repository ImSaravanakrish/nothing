from BD import tbot,TOKEN
import sys

try:
  tbot.start(bot_token=TOKEN)
  
except:
  print('invalid token')
  sys.exit()
  
  
tbot.run_until_disconnected()
