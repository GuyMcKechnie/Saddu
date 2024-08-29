import asyncio
import random

import nextcord
from nextcord import *
from nextcord.ext import commands

authorName = None
authorID = None
contentA = None
contentB = None

serverID = [909525005694562384, 945255580778500127]


class SnipeAndSnipedCommands(commands.Cog, name="Snipe & Sniped Commands"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before: nextcord.Message, after: nextcord.Message):
        if after.author.bot or before.author.bot:
            pass
        else:
            global authorName, authorID, contentB, contentA

            authorName = before.author.display_name
            authorID = before.author.id
            contentB = before.content
            contentA = after.content

            await asyncio.sleep(60)

            authorName = None
            authorID = None
            contentA = None
            contentB = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: nextcord.Message):
        if message.author.bot:
            pass
        else:
            global authorName, authorID, contentA, messageID

            authorName = message.author.display_name
            authorID = message.author.id
            contentA = message.content
            messageID = message.id

            await asyncio.sleep(60)

            authorName = None
            authorID = None
            contentA = None

    # Snipe command

    @nextcord.slash_command(name="snipe",
                            description="Snipe a deleted/edited message",
                            guild_ids=serverID)
    async def sniperCommand(self, interaction: nextcord.Interaction):
        colours = [0xeb05e3, 0x05bdeb]
        if contentA is None:
            pass
        elif contentB is None:
            if contentA is None:
                await interaction.send("There is nothing to snipe!")
            else:
                embed = Embed(title=f"Sniped {authorName}",
                              description=f"Deleted Message: {contentA}",
                              colour=random.choice(colours))
                await interaction.send(embed=embed)
        else:
            embed = Embed(title=f"Sniped {authorName}",
                          description=f"Original Message: {
                              contentB}\nEdited Message: {contentA}",
                          colour=random.choice(colours))
            await interaction.send(embed=embed)

    @commands.command()
    async def snipe(self, ctx):
        await ctx.send(
            "Command initiated commands have been discontinued. Please use /commands instead.\nExample: /snipe")

    @commands.command()
    async def sniped(self, ctx):
        await ctx.send(
            "Command initiated commands have been discontinued. Please use /commands instead.\nExample: /snipe")


def setup(client: commands.Bot):
    client.add_cog(SnipeAndSnipedCommands(client))
