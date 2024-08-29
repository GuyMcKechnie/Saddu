import nextcord
import os
import asyncio
import ffmpeg
import random
import json
from nextcord import *
from nextcord.ext import commands
from nextcord.ext.commands import *
from datetime import datetime


class MainCounting(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @commands.Cog.listener()
    @commands.cooldown(rate=10, per=10.00, type=commands.BucketType.guild)
    async def on_message(self, message: Message):
        if message.channel.id == 964947678905659442 and not message.author.bot:
            try:

                # Entered number
                num = int(message.content)
                countingChannel = self.client.get_channel(
                    964947678905659442)  # Counting channel

                # Number
                f = open("/home/container/Cogs/Counting/CountingDatabase.json")
                data = json.load(f)
                number = int(data[0])

                # Author ID
                fl = open(
                    "/home/container/Cogs/Counting/AuthorCountingDatabase.json")
                flData = json.load(fl)
                authorID = int(flData[0])

                # Check points
                cpFile = open(
                    "/home/container/Cogs/Counting/CheckPoints.json", 'r')
                cpData = json.load(cpFile)
                checkPoint = int(cpData[0])

                # Colours
                colours = [0xeb05e3, 0x05bdeb]

                if not authorID == message.author.id:  # If author is not previous counter
                    if num == number+1:  # Correct number
                        numberDict = [number+1]  # Updating number

                        with open("/home/container/Cogs/Counting/CountingDatabase.json", "w") as outfile:
                            json.dump(numberDict, outfile)

                        await message.add_reaction("✔")

                        # Updating author ID
                        authorIDUpdate = [message.author.id]
                        with open("/home/container/Cogs/Counting/AuthorCountingDatabase.json", "w") as outfile:
                            json.dump(authorIDUpdate, outfile)

                        # Updating check points
                        checkpoints = [100, 200, 300, 400,
                                       500, 600, 700, 800, 900, 1000]
                        for checkpoint in checkpoints:
                            if num == checkpoint:
                                await message.add_reaction("🎓")

                                cpFile = open(
                                    "/home/container/Cogs/Counting/CheckPoints.json", 'r')
                                cpData = json.load(cpFile)
                                checkPoint = int(cpData[0])

                                with open("/home/container/Cogs/Counting/CheckPoints.json", "w") as cpFileD:
                                    json.dump([checkPoint+1], cpFileD)
                                print(checkPoint+1)
                                break

                    elif num is not number+1:  # Incorrect number

                        colours = [0xeb05e3, 0x05bdeb]
                        embed = Embed(title="Sicarius Counting Machine 2000",
                                      description=f"{message.author.mention} counted to {
                                          str(num)}\n\nUnfortunately, they cannot count.",
                                      colour=random.choice(colours),
                                      timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=message.author.avatar.url)
                        embed.set_footer(text=f"{message.author.display_name}#{
                                         message.author.discriminator}", icon_url=message.author.avatar.url)
                        await countingChannel.send(embed=embed)

                        # Checking check point counter
                        cpFile = open(
                            "/home/container/Cogs/Counting/CheckPoints.json", 'r')
                        cpData = json.load(cpFile)
                        checkPoint = int(cpData[0])
                        if checkPoint > 0:
                            # Check Points (Taking away points if able to)
                            with open("/home/container/Cogs/Counting/CheckPoints.json", "w") as cpFileD:
                                checkPoint = [checkPoint-1]
                                json.dump(checkPoint, cpFileD)
                            embed = Embed(title="Sicarius Counting Machine 2000",
                                          description=f"The server has a check point available. It has been used and the number has not been reset!.\nCheckpoints available: {
                                              checkPoint}\nCurrent Number: {number+1}",
                                          colour=random.choice(colours),
                                          timestamp=datetime.utcnow())
                            await countingChannel.send(embed=embed)
                        elif checkPoint <= 0:
                            # Check points
                            with open("/home/container/Cogs/Counting/CheckPoints.json", "w") as cpFileD:
                                checkPoint = [0]
                                json.dump(checkPoint, cpFileD)
                            # Updating counter
                            numberDict = [0]  # Resetting number to 0
                            with open("/home/container/Cogs/Counting/CountingDatabase.json", "w") as outfile:
                                json.dump(numberDict, outfile)
                            # Updating author ID
                            authorIDUpdate = [925934213029589062]
                            with open("/home/container/Cogs/Counting/AuthorCountingDatabase.json", "w") as outfile:
                                json.dump(authorIDUpdate, outfile)
                            # Confirmation Message
                            embed = Embed(title="Sicarius Counting Machine 2000",
                                          description=f"The server has no check point available. The number has been reset to 0.",
                                          colour=random.choice(colours),
                                          timestamp=datetime.utcnow())
                            await countingChannel.send(embed=embed)

                        # Incorrect identifier
                        loggingChannel = self.client.get_channel(
                            955776300776300594)
                        embed = Embed(title="Counting Error",
                                      description=f"{message.author.name}{message.author.discriminator} counted incorrectly to {
                                          str(num)} when the number was {number+1}",
                                      timestamp=datetime.utcnow())
                        await loggingChannel.send(embed=embed)

                elif authorID == message.author.id:
                    await message.add_reaction("⏰")  # Original message
                    embed = Embed(title="Error",
                                  description="A user can only count once per number.",
                                  timestamp=datetime.utcnow())
                    errorEmbed = await countingChannel.send(embed=embed)

                    # Checking check point counter
                    cpFile = open(
                        "/home/container/Cogs/Counting/CheckPoints.json", 'r')
                    cpData = json.load(cpFile)
                    checkPoint = int(cpData[0])
                    if checkPoint > 0:
                        # Check Points
                        with open("/home/container/Cogs/Counting/CheckPoints.json", "w") as cpFileD:
                            checkPoint = [checkPoint-1]
                            json.dump(checkPoint, cpFileD)
                        embed = Embed(title="Sicarius Counting Machine 2000",
                                      description=f"The server has a check point available. It has been used.\nCheckpoints available: {
                                          checkPoint}",
                                      colour=random.choice(colours),
                                      timestamp=datetime.utcnow())
                        await countingChannel.send(embed=embed)
                    elif checkPoint <= 0:
                        # Check points
                        with open("/home/container/Cogs/Counting/CheckPoints.json", "w") as cpFileD:
                            checkPoint = [0]
                            json.dump(checkPoint, cpFileD)
                        # Updating counter
                        numberDict = [0]  # Resetting number to 0
                        with open("/home/container/Cogs/Counting/CountingDatabase.json", "w") as outfile:
                            json.dump(numberDict, outfile)
                        # Updating author ID
                        authorIDUpdate = [925934213029589062]
                        with open("/home/container/Cogs/Counting/AuthorCountingDatabase.json", "w") as outfile:
                            json.dump(authorIDUpdate, outfile)
                        # Confirmation Message
                        embed = Embed(title="Sicarius Counting Machine 2000",
                                      description=f"The server has no check point available. The number has been reset to 0.",
                                      colour=random.choice(colours),
                                      timestamp=datetime.utcnow())
                        await countingChannel.send(embed=embed)

                    # Incorrect identifier
                    loggingChannel = self.client.get_channel(
                        955776300776300594)
                    embed = Embed(title="Counting Error",
                                  description=f"{message.author.name}{message.author.discriminator} counted incorrectly to {
                                      str(num)} when the number was {number+1}",
                                  timestamp=datetime.utcnow())
                    await loggingChannel.send(embed=embed)

                    f.close()
                    fl.close()

            except ValueError:
                if not message.author.bot:
                    pass


def setup(client: commands.Bot):
    client.add_cog(MainCounting(client))
