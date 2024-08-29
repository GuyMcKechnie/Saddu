import asyncio
import datetime
import random

import nextcord
import requests
from nextcord import *
from nextcord.ext import commands

serverID = [909525005694562384, 945255580778500127]


class FunCommands(commands.Cog, name="Fun Commands"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @nextcord.slash_command(description="Insult a user",
                            guild_ids=serverID)
    async def insult(self, act: Interaction, member: Member = SlashOption(required=True)):
        colours = [0xeb05e3, 0x05bdeb]
        insult_request = requests.get(
            "https://evilinsult.com/generate_insult.php?lang=en&type=json")
        if not member.bot:
            if 300 > insult_request.status_code >= 200:
                content = insult_request.json()
                insult = content["insult"]
                embed = Embed(title=f"{act.user.display_name} roasted {member.display_name}",
                              description=f"{insult}",
                              colour=random.choice(colours))
                await act.send(embed=embed)
        elif member.bot:
            await act.send("I will never insult my kind!")

    @nextcord.slash_command(description="Measure the penis size of a member",
                            guild_ids=serverID)
    async def penis(self, act: Interaction, member: Member = SlashOption(required=True)):
        colours = [0xeb05e3, 0x05bdeb]
        penis_sizes = ["〓",
                       "〓〓〓",
                       "〓〓〓〓〓",
                       "〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓",
                       "〓too small to measure〓"]
        embed = Embed(title=f"**{member.name}'s Penis Size**",
                      description=f"◯\n  │   {random.choice(penis_sizes)}☽\n◯",
                      colour=random.choice(colours))
        await act.send(embed=embed)

    @nextcord.slash_command(description="Say something with the bot.",
                            guild_ids=serverID)
    async def say(self, interaction: Interaction,
                  content: str = SlashOption(required=True, description="Message to say")):
        await interaction.send(str(content))

    @nextcord.slash_command(description="Fetch your current ping",
                            guild_ids=serverID)
    async def ping(self, intact: Interaction):
        colours = [0x05bdeb, 0xeb05e3]
        embed = Embed(title=f"Your Ping Is:",
                      description=f"**{round(self.client.latency * 1000)}ms**",
                      timestamp=datetime.datetime.utcnow(),
                      colour=random.choice(colours))
        embed.set_footer(text="/ping", icon_url=intact.user.avatar)
        await intact.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(FunCommands(client))
