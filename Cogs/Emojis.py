import nextcord
from nextcord import *
from nextcord.ext import commands


class Emojis(commands.Cog, name="Emojis"):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(name="emoji", description="Send any animated emoji in the Sicarius discord server",
                            guild_ids=serverID)
    async def emoji(self, interaction: Interaction,
                    emoji: str = SlashOption(name="emoji",
                                             description="Enter an animated emoji name from the Sicarius discord server",
                                             required=True)):
        if emoji == "200iq":
            fetchedEmoji = self.client.get_emoji(926053534225535016)
            await interaction.send(fetchedEmoji)
        elif emoji == "abdullah":
            fetchedEmoji = self.client.get_emoji(926054984318058506)
            await interaction.send(fetchedEmoji)
        elif emoji == "birdfap":
            fetchedEmoji = self.client.get_emoji(931886330227601439)
            await interaction.send(fetchedEmoji)
        elif emoji == "cringe":
            fetchedEmoji = self.client.get_emoji(926053311654801418)
            await interaction.send(fetchedEmoji)
        elif emoji == "fire~1":
            fetchedEmoji = self.client.get_emoji(926055487814893569)
            await interaction.send(fetchedEmoji)
        elif emoji == "kek" or emoji == "kekw":
            fetchedEmoji = self.client.get_emoji(919321967465750578)
            await interaction.send(fetchedEmoji)
        elif emoji == "pepehit":
            fetchedEmoji = self.client.get_emoji(926053678165663795)
            await interaction.send(fetchedEmoji)
        elif emoji == "pepesimp":
            fetchedEmoji = self.client.get_emoji(955820542559150100)
            await interaction.send(fetchedEmoji)
        elif emoji == "pepeshoot":
            fetchedEmoji = self.client.get_emoji(955819807708692560)
            await interaction.send(fetchedEmoji)
        elif emoji == "pepesaber":
            fetchedEmoji = self.client.get_emoji(955523117801951362)
            await interaction.send(fetchedEmoji)
        elif emoji == "rickroll":
            fetchedEmoji = self.client.get_emoji(955821392723591248)
            await interaction.send(fetchedEmoji)
        elif emoji == "snapped":
            fetchedEmoji = self.client.get_emoji(944867350753206302)
            await interaction.send(fetchedEmoji)
        elif emoji == "wait":
            fetchedEmoji = self.client.get_emoji(926053027683635270)
            await interaction.send(fetchedEmoji)
        elif emoji == "trollege":
            fetchedEmoji = self.client.get_emoji(955821859482517524)
            await interaction.send(fetchedEmoji)
        elif emoji == "think":
            fetchedEmoji = self.client.get_emoji(926053796847702036)
            await interaction.send(fetchedEmoji)
        elif emoji == "weewoo":
            fetchedEmoji = self.client.get_emoji(926052897832189973)
            await interaction.send(fetchedEmoji)
        elif emoji == "yoshi":
            fetchedEmoji = self.client.get_emoji(926053451765542972)
            await interaction.send(fetchedEmoji)
        else:
            await interaction.send(
                f"No emoji with the name {emoji} found!\nFor the list of usable emojis type /emojis.")

    @nextcord.slash_command(description="Returns a list of usable emojis with the /emoji command.",
                            guild_ids=serverID)
    async def emojis(self, interaction: Interaction):
        global emoji1
        emojiList = []
        for emoji1 in self.client.emojis:
            if emoji1.animated:
                emojiList.append(str(emoji1.name))
        embed = Embed(title="List of usable emojis with the /emoji command:")
        for emojis in emojiList:
            embed.add_field(name=f"Name: *{emojis}*", value=f"ID: *{emoji1.id}*", inline=False)
        await interaction.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if not message.author.bot:
            if "kek" in message.content or "kekw" in message.content or "Kekw" in message.content or "Kek" in message.content:
                fetchedEmoji = self.client.get_emoji(919321967465750578)
                await message.channel.send(fetchedEmoji)
            if "yoshi" in message.content:
                fetchedEmoji = self.client.get_emoji(926053451765542972)
                await message.channel.send(fetchedEmoji)


def setup(client: commands.Bot):
    client.add_cog(Emojis(client))
