# This example requires the 'message_content' intent.
from modules.extra import extra as e
import discord

from modules.ollama import ollama

ki = ollama()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.endswith('??'):
        print(message.content)
        reply = ki.ask(message.content)
        print(reply)
        await message.channel.send(reply)

client.run(e.readToken("IRS.token"))
