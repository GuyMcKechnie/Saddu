import random
from datetime import datetime

import nextcord
from nextcord import *
from nextcord.ext import commands

serverID = [909525005694562384, 945255580778500127]


class Suggestions(commands.Cog, name="Suggestion Command"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @nextcord.slash_command(description="Suggest something to add to / change about / remove from the server",
                            guild_ids=serverID)
    async def suggest(self, interaction: Interaction,
                      suggestion: str = SlashOption(required=True, description="Enter your suggestion.")):
        if suggestion == "":
            await interaction.send("You cannot enter a blank suggestion!")
        colours = [0xeb05e3, 0x05bdeb]

        suggestionChannel = self.client.get_channel(934387354477662238)
        suggestionRole = nextcord.utils.get(
            interaction.guild.roles, id=934448217549053982)
        emoji1 = self.client.get_emoji(919325690095075329)
        emoji2 = self.client.get_emoji(919325703940481034)
        emojiWeeWoo = self.client.get_emoji(926052897832189973)

        embed = Embed(title="Server Suggestion",
                      description=f"Suggestion by {
                          interaction.user.mention}:\n{suggestion}.",
                      colour=random.choice(colours),
                      timestamp=datetime.utcnow())
        suggestionMessage = await suggestionChannel.send(f"Attention {suggestionRole.mention}{emojiWeeWoo}",
                                                         embed=embed)
        await suggestionMessage.add_reaction(emoji1)
        await suggestionMessage.add_reaction(emoji2)

        await interaction.send("Suggestion sent successfully!")


def setup(client: commands.Bot):
    client.add_cog(Suggestions(client))
