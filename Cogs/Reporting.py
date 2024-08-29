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


class BugReports(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description="Reports a member to the administrators",
                            guild_ids=serverID)
    async def report(self, act: Interaction, user: Member, report):
        adminChannel = self.client.get_channel(926018129971249162)
        adminRole = nextcord.utils.get(act.guild.roles, id=944932139139465267)

        embed = Embed(title="User Report",
                      description=f"Submitter: {act.user.display_name}#{act.user.discriminator}\nReport: {
                          report}\nTarget: {user.display_name}#{user.discriminator}",
                      timestamp=datetime.utcnow())
        await adminChannel.send(f"New report, {adminRole.mention}", embed=embed)
        await act.send("Sent report successfully")

    @nextcord.slash_command(description="Reports a bug to the developers",
                            guild_ids=serverID)
    async def bugreport(self, act: Interaction, bug):
        ping = await self.client.fetch_user(681003604869644331)
        nanasToy = self.client.get_channel(932655328359743548)

        embed = Embed(title="Bug Report",
                      description=f"Reporter: {act.user.display_name}#{
                          act.user.discriminator}\nBug: {bug}",
                      timestamp=datetime.utcnow())
        await nanasToy.send(f"{ping.mention}", embed=embed)
        await act.send("Sent report successfully")


def setup(client: commands.Bot):
    client.add_cog(BugReports(client))
