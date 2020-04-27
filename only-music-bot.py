import os

import discord
import re
import time
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

valid_expressions = [
    re.compile('^\-play .*$', re.IGNORECASE),
    re.compile('^\-next', re.IGNORECASE),
    re.compile('^\-stop', re.IGNORECASE)
]

client = discord.Client()

@client.event
async def on_message(message):
    wait = False
    if str(message.author) == 'Groovy#7254':
        return

    for expression in valid_expressions:
        wait = wait or not expression.match(message.content)
    if wait:
        time.sleep(5)    
    await message.delete()
    


client.run(TOKEN)