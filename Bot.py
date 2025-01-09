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
        # @self.client.command("help")
        # async def help_command(ctx):
        #     help_message= """
        #     **Bot Commands:**
        #     - `!help`: Show this help message.
        #     - `!join`: Make the bot join your current voice channel.
        #     - `!write <message>`: The bot will write the specified message in the chat.
        #     """
        #     await ctx.send(help_message)
    
        @self.client.command("join")
        async def join(ctx):
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
                print(f"Joined {channel}")
            else:
                print(f"Konnte nicht beitreten, da {ctx.author} in keinem VC ist")

        @self.client.command("leave")
        async def leave(ctx):
            if ctx.voice_client:
                await ctx.voice_client.disconnect()
                # print(f"Disconnected von {ctx.voice_client.channel}")
            else:
                await print(f"Derzeit in keinem VC")

        @self.client.command("write")
        async def write(ctx, *, message: str):
            await ctx.send(message)

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

        @self.client.command("play")
        async def play(ctx,*,message:str):
            voice = ctx.voice_client
            message = message.lower()
            try:
                if voice:        
                    # if message.find("youtube"):
                    if "youtube" in message:
                        print(message)
                        # self.e.y_link(message)
                        await ctx.send(f"Spiele {message} ab")
                        path = os.path.join(self.e.getDPath(),"test.mp3")
                        print(path)
                        voice.play(
                            discord.FFmpegPCMAudio(
                                path), after=lambda e: print(f"Fehler: {e}") if e else None)
                    else:
                        await ctx.send("Fehler, kein YouTube Link")
                else:
                    await ctx.send("Lasse mich zu erst einem Voice Chat beitreten")
            except Exception as e:
                print(e)


    def runBot(self):
        self.client.run(self.e.readToken("IRS.token"))

if __name__ == "__main__":
    irs = Bot()
    irs.runBot()
