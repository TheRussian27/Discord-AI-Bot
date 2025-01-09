from modules.extra import extra
from modules.ollama import ollama
import discord
from discord.ext import commands#
import os
from pathlib import Path as p

class Bot:
    def __init__(self):
        self.ki = ollama()
        self.e = extra()
        self.client = commands.Bot(command_prefix="?",intents = self.__setIntents())
        self.setup_events()
        self.setup_commands()

    def __setIntents(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        return intents

    def setup_events(self):
        
        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')

    def setup_commands(self):
        @self.client.command("ask")
        async def ask(ctx, *, message:str):
            reply = self.ki.ask(message)
            await ctx.send(reply)

        @self.client.command("reset-ki")
        async def resetKI(ctx):
            self.ki.resetChatHistory()
            await ctx.send("Die Bot Historie wurde zurückgesetzt")

        @self.client.command("surprise")
        async def suprise(ctx):
            path = str(p(__file__).resolve().parent)
            with open(path + "/media/images/jonkler.png", "rb") as f:
                pic = discord.File(f)
            await ctx.send(file=pic)


    def runBot(self):
        self.client.run(self.e.readToken("IRS.token"))

if __name__ == "__main__":
    irs = Bot()
    irs.runBot()
