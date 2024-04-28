import os

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
nextcord.members = True

client = commands.Bot(command_prefix="s-", intents=intents, help_command=None)

for fn in os.listdir("./Cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.{fn[:-3]}")

for fn in os.listdir("./Cogs/ProfileLib"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.ProfileLib.{fn[:-3]}")

for fn in os.listdir("./Cogs/MessageCount"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.MessageCount.{fn[:-3]}")
    
for fn in os.listdir("./Cogs/Music"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.Music.{fn[:-3]}")

for fn in os.listdir("./Cogs/TTS"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.TTS.{fn[:-3]}")

for fn in os.listdir("./Cogs/Counting"):
    if fn.endswith(".py"):
        client.load_extension(f"Cogs.Counting.{fn[:-3]}")

client.run("TOKEN")
