from modules.extra import extra as e
from modules.ollama import ollama
import discord

#Ki wird angebunden
ki = ollama()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@968437674396483585>'):
        reply = ki.ask(message.content)
        await message.channel.send(reply)

client.run(e.readToken("IRS.token"))
