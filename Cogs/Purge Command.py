import asyncio
from datetime import datetime

import nextcord
from nextcord import *
from nextcord.ext import commands


class Purge(commands.Cog, name="Purge Command"):

    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(name="purge",
                            description="Purge a given amount of messages",
                            guild_ids=serverID)
    async def purgeCommand(self, interaction: Interaction, amount: int = SlashOption(required=True)):
        if interaction.user.guild_permissions.administrator:
            amount = amount
            if amount >= 100:
                await interaction.send(
                    f"Purging {
                        amount} messages. This is a large amount of messages. It might take a while!",
                    delete_after=1)
                await asyncio.sleep(2)
                channel = interaction.channel
                await channel.purge(limit=amount)
                await interaction.send("Purge completed successfully!", delete_after=5)
                logChannel = self.client.get_channel(955776300776300594)
                embed = Embed(title="Purge Command Initiated",
                              description=f"Author: {interaction.user.name}{
                                  interaction.user.discriminator}\n"
                              f"Purge Amount: {amount}\n"
                              f"Time: {datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
                await logChannel.send(embed=embed)
            else:
                await interaction.send(
                    f"Purging {amount} messages.", delete_after=1)
                await asyncio.sleep(2)
                channel = interaction.channel
                await channel.purge(limit=amount)
                await interaction.send("Purge completed successfully!", delete_after=5)
                logChannel = self.client.get_channel(955776300776300594)
                embed = Embed(title="Purge Command Initiated",
                              description=f"Author: {interaction.user.name}{
                                  interaction.user.discriminator}\n"
                              f"Purge Amount: {amount}\n"
                              f"Time: {datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
                await logChannel.send(embed=embed)
        else:
            await interaction.send("You do not have permission to do that!", delete_after=2)


def setup(client: commands.Bot):
    client.add_cog(Purge(client))
