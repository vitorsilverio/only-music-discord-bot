import os

import discord
import re
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
    delete = True
    if str(message.author) == 'Groovy#7254':
        delete = False

    for expression in valid_expressions:
        delete = delete and not expression.match(message.content)
    if delete:
        await message.delete()


client.run(TOKEN)