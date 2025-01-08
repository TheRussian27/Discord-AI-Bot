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

    #Wenn der Bot gepingt wird, soll er antworten
    if message.content.startswith('<@968437674396483585>'):
        txt = message.content                               
        i_del = txt.index(" ") + 1                          #Variable zum bestimmen, wann @Bot endet da dieser die Pings nicht interpretieren 
        txt = txt[i_del:]
        reply = ki.ask(txt)
        await message.channel.send(reply)

    #Wenn der "Befehl" eingegeben wird, soll der Bot resettet werden
    if message.content.startswith(".bot reset"):
        ki.resetChatHistory()
        await message.channel.send("Die Bot Historie wurde zurückgesetzt")

client.run(e.readToken("IRS.token"))