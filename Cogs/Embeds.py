import datetime
import nextcord
import random

from nextcord import *
from nextcord.ext import commands


class Embeds(commands.Cog, name="Embeds"):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description="Returns a list of rules used in the server",
                            guild_ids=serverID)
    async def rules(self, act: Interaction):
        if act.user.guild_permissions.administrator:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)
            rulesEmbed = Embed(title="❈ __Rules__ ❈",
                               description="*These are not definitive rules, but community guidelines. These can "
                               "be changed at any given time.*",
                               color=colour_choice,
                               timestamp=datetime.datetime.utcnow())
            rulesEmbed.add_field(name="1. Follow all the rules",
                                 value="The rules are there to be followed and you are expected to do so. They are simple "
                                 "and they do not confine members.",
                                 inline=False)
            rulesEmbed.add_field(name="2. Respect",
                                 value="It is expected of you to respect fellow members of the discord server as well as "
                                 "yourself.",
                                 inline=False)
            rulesEmbed.add_field(name="3. Spamming",
                                 value="Spamming will not be tolerated on an exaggerated extent. It is not confining in "
                                 "the way that it still provides users who type fast a normal chatting experience. "
                                 "Sending of multiple, similar messages will not be tolerated. Spam pinging for no "
                                 "/ unnecessary reasoning will also not be tolerated. Members with the @everyone "
                                 "ping who abuse this permission will be dealt with promptly.",
                                 inline=False)
            rulesEmbed.add_field(
                name="4. Swearing", value="Swearing is allowed but keep it to a low.", inline=False)
            rulesEmbed.add_field(name="5. Channels",
                                 value="Use channels for their intended purposes: Channels are there for a purpose, "
                                 "so ensure you do not mix-and-match channels and their uses. And don't get annoyed "
                                 "when someone asks you to please stop abusing the channels. Before asking for a "
                                 "channel to be added ensure you go through the entire Discord server and check to "
                                 "see if there is already a channel for your desired purpose.",
                                 inline=False)
            rulesEmbed.add_field(name="6. Gore",
                                 value="Kids are a thing, and with kids come impressionable minds. Do not open these "
                                 "minds up to traumatic images/videos or encourage them to do so. This includes "
                                 "anything to do with animals and any other life.",
                                 inline=False)
            rulesEmbed.add_field(name="7. Role Abuse",
                                 value="If you are are given a role with permissions higher than anyone else's and you "
                                 "abuse these permissions your role will be removed from you. Depending on the "
                                 "offense more action will be taken, e.g., muting, banning etc..",
                                 inline=False)
            rulesEmbed.add_field(name="8. Anything To Do With Hacking",
                                 value="This server has no affiliation (or desire to have any affiliation) with token "
                                 "logging, IP grabbing, personal information leaking or any other form of harmful "
                                 "act. Do not use this server and its members as test dummies for your IP grabber. "
                                 "Bans will be laid out, no exceptions.",
                                 inline=False)
            rulesEmbed.set_footer(text="Sicarius Discord Administrators ",
                                  icon_url=act.guild.icon.url)

            await act.send(embed=rulesEmbed)
        else:
            await act.send("You do not have permission to do that!")

    @nextcord.slash_command(description="Returns a list of Sicarius CTF members and scrim participants",
                            guild_ids=serverID)
    async def members(self, act: Interaction):
        if act.user.guild_permissions.administrator:
            colours = [0xeb05e3, 0x05bdeb]
            tierOnes = "◯ Srcheddarchz\n◯ ghoul3953\n◯ JASONPROGAMER57\n◯ nightclxy\n◯ Ghostinasia\n vqpecliennt"
            tierTwos = "◯ Ghoulinasia\n◯ ItzMiri"
            tierThrees = "◯ NotKaizar\n◯ RefundingPanic\n◯ NoSwagPanda"
            tierFours = "◯ oAx3LLo\n◯ breezxie\n◯ xFazeCool\n◯ MaRcUz6571\n◯ xNitrqx1\n◯ SmqrtRaccoon\n◯ OiStove"
            scrimParts = "◯ ghoul3953\n◯ xNitrqx1\n◯ vqpecliennt\n◯ JASONPROGAMER57\n◯ ItzMiri\n◯ xFazeCool\n◯ Srcheddarchz\n◯ OiStove\n◯ NoSwagPanda\n◯ RefundingPanic"
            membersEmbed = Embed(title="❈ __Sicarius CTF Members__ ❈",
                                 description=f"",
                                 colour=random.choice(colours),
                                 timestamp=datetime.datetime.utcnow())
            membersEmbed.add_field(
                name=f"**Tier 1 Members**", value=f">>> {tierOnes}", inline=False)
            membersEmbed.add_field(
                name=f"**Tier 2 Members**", value=f">>> {tierTwos}", inline=False)
            membersEmbed.add_field(
                name=f"**Tier 3 Members**", value=f">>> {tierThrees}", inline=False)
            membersEmbed.add_field(
                name=f"**Tier 4 Members**", value=f">>> {tierFours}", inline=False)
            membersEmbed.add_field(
                name=f"\n**__Scrim Participants__**", value=f">>> {scrimParts}", inline=False)
            await act.send(embed=membersEmbed)
        else:
            await act.send("You do not have permission to use this command!")

    @nextcord.slash_command(description="Saddu's feature list",
                            guild_ids=serverID)
    async def features(self, act: Interaction):
        colours = [0xeb05e3, 0x05bdeb]
        saddu: Member = self.client.get_user(925934213029589062)
        if act.user.guild_permissions.administrator:
            embed = Embed(title="**__Saddu's Feature List__**",
                          description=f"For a full list of {
                              saddu.mention}'s features use: /help\n\n",
                          colour=random.choice(colours),
                          timestamp=datetime.datetime.utcnow())
            features = [("__Levelling System__:", "A fully functional levelling system to replace the existing levelling system. Features that will be included should replace and update the existing levelling system."),
                        ("__Better Music System__:",
                         "A better functioning music system. Features that will be included:\n> Spotify Integration."),
                        ("__Counting System__:", "A fully functional counting system to replace the existing couting system. Features that will be included:\n> ~~Automatic saving points.~~\n> ~~1-number-per-person counting system.~~ *Under Testing*\n> Rewards based off participation."),
                        ("__Reaction Roles__:",
                         "A sophisticated reaction roles to replace the existing reaction roles."),
                        ("__Starboard System__:", "A complex starboard system to replace the existing starboard system. Features that will be included:\n> Self-message starring.")]
            for name, value in features:
                embed.add_field(name=name, value=f">>> {value}", inline=False)
            await act.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Embeds(client))
