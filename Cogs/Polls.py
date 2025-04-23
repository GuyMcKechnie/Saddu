import random

import nextcord
from nextcord import *
from nextcord.ext import commands


class Polls(commands.Cog, name="Poll Commands"):

    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(name="pollone",
                            description="Poll for yes and no options. Option 1 is yes, option 2 is no",
                            guild_ids=serverID)
    async def pollone(self, interaction: Interaction,
                      option1: str = SlashOption(required=True),
                      option2: str = SlashOption(required=True),
                      question: str = SlashOption(required=True)):
        if interaction.user.guild_permissions.administrator:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)

            yesEmoji = self.client.get_emoji(919325690095075329)
            noEmoji = self.client.get_emoji(919325703940481034)

            pollChannel = self.client.get_channel(926018110459355176)
            pollMention = nextcord.utils.get(
                interaction.guild.roles, id=927069041334554645)
            emoji = self.client.get_emoji(926052897832189973)

            embed = Embed(title="New Poll",
                          description=f"**{question}**", colour=colour_choice)
            embed.add_field(name=f"To vote for: {option1}", value=f"React with {yesEmoji} below", inline=True)
            embed.add_field(name=f"To vote for: {option2}", value=f"React with {noEmoji} below", inline=True)

            message = await pollChannel.send(f"Attention {pollMention.mention}{emoji}", embed=embed)
            await message.add_reaction(yesEmoji)
            await message.add_reaction(noEmoji)

            await interaction.send("Poll sent successfully!")

        else:
            await interaction.send("You do not have permission to send polls!")

    @nextcord.slash_command(name="polltwo",
                            description="Poll for two options",
                            guild_ids=serverID)
    async def polltwo(self, interaction: Interaction,
                      option1: str = SlashOption(required=True),
                      option2: str = SlashOption(required=True),
                      question: str = SlashOption(required=True)):
        if interaction.user.guild_permissions.administrator:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)

            optionOneEmoji = self.client.get_emoji(945349456738529341)
            optionTwoEmoji = self.client.get_emoji(945349457258635286)

            pollChannel = self.client.get_channel(926018110459355176)
            pollMention = nextcord.utils.get(
                interaction.guild.roles, id=927069041334554645)
            emoji = self.client.get_emoji(926052897832189973)

            embed = Embed(title="New Poll",
                          description=f"**{question}**", colour=colour_choice)
            embed.add_field(name=f"To vote for: {option1}", value=f"React with {optionOneEmoji} below", inline=True)
            embed.add_field(name=f"To vote for: {option2}", value=f"React with {optionTwoEmoji} below", inline=True)

            message = await pollChannel.send(f"Attention {pollMention.mention}{emoji}", embed=embed)
            await message.add_reaction(optionOneEmoji)
            await message.add_reaction(optionTwoEmoji)

            await interaction.send("Poll sent successfully!")

        else:
            await interaction.send("You do not have permission to send polls!")

    @nextcord.slash_command(name="pollthree",
                            description="Poll for three options",
                            guild_ids=serverID)
    async def pollthree(self, interaction: Interaction,
                        option1: str = SlashOption(required=True),
                        option2: str = SlashOption(required=True),
                        option3: str = SlashOption(required=True),
                        question: str = SlashOption(required=True)):
        if interaction.user.guild_permissions.administrator:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)

            optionOneEmoji = self.client.get_emoji(945349456738529341)
            optionTwoEmoji = self.client.get_emoji(945349457258635286)
            optionThreeEmoji = self.client.get_emoji(945349457418018816)

            pollChannel = self.client.get_channel(926018110459355176)
            pollMention = nextcord.utils.get(
                interaction.guild.roles, id=927069041334554645)
            emoji = self.client.get_emoji(926052897832189973)

            embed = Embed(title="New Poll",
                          description=f"**{question}**", colour=colour_choice)
            embed.add_field(name=f"To vote for: {option1}", value=f"React with {optionOneEmoji} below", inline=False)
            embed.add_field(name=f"To vote for: {option2}", value=f"React with {optionTwoEmoji} below", inline=False)
            embed.add_field(name=f"To vote for: {option3}", value=f"React with {optionThreeEmoji} below", inline=False)

            message = await pollChannel.send(f"Attention {pollMention.mention}{emoji}", embed=embed)
            await message.add_reaction(optionOneEmoji)
            await message.add_reaction(optionTwoEmoji)
            await message.add_reaction(optionThreeEmoji)

            await interaction.send("Poll sent successfully!")

        else:
            await interaction.send("You do not have permission to send polls!")


def setup(client: commands.Bot):
    client.add_cog(Polls(client))
