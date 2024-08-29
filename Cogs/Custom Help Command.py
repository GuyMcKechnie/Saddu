import random
from datetime import datetime

import nextcord
from nextcord import *
from nextcord.ext import commands


class CustomHelpCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description="Returns a list of commands available",
                            guild_ids=serverID)
    async def help(self, act: Interaction, group: str = SlashOption(required=False, description="Leave open to receive the full list command groups")):
        colours = [0xeb05e3, 0x05bdeb]
        if group is None:
            embed = Embed(title="**Sicarius Discord Server Commands**",
                          description="",
                          colour=random.choice(colours),
                          timestamp=datetime.utcnow())
            embed.add_field(name="Please enter which category you would like to display:",
                            value="✢ Fun Commands\n"
                            "✢ Message Counters\n"
                            "✢ Music\n"
                            "✢ Text-To-Speech: Use `TTS` or `tts`\n"
                            "✢ Profiles\n"
                            "✢ Snipe\n"
                            "✢ Suggestions\n"
                            "✢ Emojis\n",
                            inline=False)
            embed.add_field(name="For example:",
                            value="/help Fun Commands", inline=False)
            await act.send(embed=embed)

        elif group == "Fun Commands" or group == "fun commands" or group == "Fun commands" or group == "fun Commands":
            funCommands = "**Insult**: Enter /`insult` (person's name) to insult them! A random insult is thrown at the mentioned person.\n\n" \
                          "**Penis**: Enter /`penis` (person's name) to measure their penis size! An accurate representation of the user's penis will be returned.\n\n" \
                          "**Horny**: Enter /`horny` (person's name) to generate a Horny Pass! An overlay will be generated with the person's icon.\n\n" \
                          "**Joke**: Enter /`joke` to receive a random joke! A random joke will be sent.\n\n" \
                          "**Say**: Enter /`say` to say something using the bot.\n\n" \
                          "**Leave**: Enter /`leave` to leave the chat.\n\n" \
                          "**Quote**: Enter /`quote` to receive a random quote.\n\n" \
                          "**Ping**: Enter /`ping` to receive the bots ping."
            funEmbed = Embed(title="__**Fun Commands:**__",
                             description=f">>> {funCommands}",
                             colour=random.choice(colours),
                             timestamp=datetime.utcnow())
            funEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=funEmbed)

        elif group == "Message Counters" or group == "message counters" or group == "count" or group == "msgcount":
            messageCountCommands = "**Message Count**: Enter /`count` (person's name) to receive their message count.\n\n" \
                                   "**Server Message Count**: Enter /`scount` to receive their server message count."
            countEmbed = Embed(title="__**Message Counters**__",
                               description=f">>> {messageCountCommands}",
                               colour=random.choice(colours),
                               timestamp=datetime.utcnow())
            countEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=countEmbed)

        elif group == "Music" or group == "music":
            musicCommands = "**Play**: Enter /`play` (song's name) to play a song.\n\n" \
                "**Pause**: Enter /`pause` pause the currently playing song.\n\n" \
                "**Resume**: Enter /`resume` to resume playing the song.\n\n" \
                "**Stop**: Enter /`stop` to stop playing the song. You can enter 'y' or 'n' afterwards to disconnect the bot or not.\n\n" \
                "**Volume**: Enter /`volume` (amount % `0-100`) to change the volume of the music player. Default is 10%.\n\n" \
                "**Now Playing**: Enter /`nowplaying` to return the currently playing song."
            musicEmbed = Embed(title="__**Music**__",
                               description=f">>> {musicCommands}",
                               colour=random.choice(colours),
                               timestamp=datetime.utcnow())
            musicEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=musicEmbed)

        elif group == "TTS" or group == "tts":
            ttsCommands = "**TTS**: Enter /`tts` (message) to send a TTS message in a voice channel.\n\n"
            ttsEmbed = Embed(title="__**TTS**__",
                             description=f">>> {ttsCommands}",
                             colour=random.choice(colours),
                             timestamp=datetime.utcnow())
            ttsEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=ttsEmbed)

        elif group == "Profile Commands" or group == "profile commands" or group == "profile Commands" or group == "profile Commands" or group == "Profile commands" or group == "profiles":
            profileCommands = "**Avatar**: Enter /`avatar` (person's name) to receive their profile picture! A image of the person's profile picture will be sent.\n\n" \
                              "**Server Information**: Enter /`server` to display information about the server! Information about the Sicarius Discord server will be sent.\n\n" \
                              "**User Profile**: Enter /`profile`, (person's name) to receive the person's profile information! Information about the person will be sent."
            profileEmbed = Embed(title="__**Profile Commands**__",
                                 description=f">>> {profileCommands}",
                                 colour=random.choice(colours),
                                 timestamp=datetime.utcnow())
            profileEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=profileEmbed)

        elif group == "Snipe" or group == "snipe" or group == "snipe":
            snipeCommands = "**Snipe**: Enter /`snipe` after a message has been edited/deleted to receive the content of that message before it was edited/deleted!"
            snipeEmbed = Embed(title="__**Sniper Commands**__",
                               description=f">>> {snipeCommands}",
                               colour=random.choice(colours),
                               timestamp=datetime.utcnow())
            snipeEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=snipeEmbed)

        elif group == "Suggestions" or group == "suggestions" or group == "suggest" or group == "Suggest":
            suggestCommand = "**Suggestions**: Enter /`suggest` (suggestion) to send a suggestion! A suggestion will be sent to the suggestions channel. "
            suggestEmbed = Embed(title="__**Suggestions**__",
                                 description=f">>> {suggestCommand}",
                                 colour=random.choice(colours),
                                 timestamp=datetime.utcnow())
            suggestEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=suggestEmbed)

        elif group == "Emoji" or group == "Emojis" or group == "emoji" or group == "emojis":
            emojiCommands = "**Emojis:** Enter /`emoji` (emoji name) to send an animated emoji using the bot.\n\n" \
                            "*For a full list of usable emojis: /`emojis`*"
            emojiEmbed = Embed(title="__**Emojis**__",
                               description=f">>> {emojiCommands}",
                               colour=random.choice(colours),
                               timestamp=datetime.utcnow())
            emojiEmbed.set_footer(
                text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
            await act.send(embed=emojiEmbed)

        else:
            await act.send("No command category found with that name!")


def setup(client: commands.Bot):
    client.add_cog(CustomHelpCommand(client))
