import random
from datetime import datetime

from nextcord import *
import nextcord
from nextcord.ext import commands


class AdminHelpCommand(commands.Cog, name="Admin Help Command"):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description="Help command for Administrators",
                            guild_ids=serverID)
    async def admin(self, act: Interaction, group: str = SlashOption(required=False, description="Enter the command group name for administrators commands. Leave blank to return the list of groups")):
        colours = [0xeb05e3, 0x05bdeb]
        colour_choice = random.choice(colours)
        if act.user.guild_permissions.administrator:
            if group is None:
                embed = Embed(title="**__Sicarius Administrator Server Commands__**",
                              description="",
                              colour=colour_choice,
                              timestamp=datetime.utcnow())
                embed.set_footer(
                    text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
                embed.add_field(name="Please enter which category you would like to display:",
                                value="✢ Polls\n"
                                "✢ Purge Command\n"
                                "✢ Admin\n"
                                "✢ Embeds",
                                inline=False)
                embed.add_field(name="For example:",
                                value="/admin Polls", inline=False)
                await act.send(embed=embed)

            elif group == 'Polls' or group == 'polls' or group == 'poll' or group == 'polls':
                pollCommands = "**Yes/No Emoji Poll**: Enter /pollone to send a poll with the check and the cross emoji choices.\n" \
                               "*Parameters:* /pollone 'option1' 'option2' question.\n\n" \
                               "**1/2 Emoji Poll**: Enter /polltwo to send a poll with the emojis 1 & 2 corresponding to choices.\n" \
                               "*Parameters:* /polltwo 'option1' 'option2' question.\n\n" \
                               "**Three Options**: Enter /pollthree to send a poll similar to two_options but with 3 options.\n" \
                               "*Parameters:* /pollthree 'option1' 'option2' 'option3' question."
                pollEmbed = Embed(title="__**Poll Commands**__",
                                  description=f">>> {pollCommands}",
                                  colour=colour_choice,
                                  timestamp=datetime.utcnow())
                pollEmbed.set_footer(
                    text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
                await act.send(embed=pollEmbed)

            elif group == 'purge' or group == 'purge command' or group == 'Purge Command' or group == 'Purge':
                purgeCommands = "**Purge**: Enter /purge (amount) to purge the given amount of messages."
                purgeEmbed = Embed(title="__**Purge Commands**__",
                                   description=f">>> {purgeCommands}",
                                   colour=colour_choice,
                                   timestamp=datetime.utcnow())
                await act.send(embed=purgeEmbed)

            elif group == 'Admin' or group == 'admin':
                adminCommands = "**Default Role Additions**: Enter /addrole_default to add the roles received once a user joins the server.\n" \
                                "**CTF Role Additions**: Enter /addrole_ctfmember to add the required roles for a CTF member when they first join.\n" \
                                "**Bot Role Additions**: Enter /addrole_bot to add the required roles for a new user bot, as well as remove member roles (if they have any).\n" \
                                "**Ban**: Enter /ban to ban a member.\n" \
                                "**Unban**: Enter /unban to unban a user. Use the user's ID.\n" \
                                "**Timeout**: Enter /timeout to time a member out.\n" \
                                "**TTag**: Enter /ttag to remove the timeout tag from the member."
                adminEmbed = Embed(title="**__Administrator Commands__**",
                                   description=f"These are in the form of slash commands (/commands) and can be triggered by typing /command name.\n>>> {adminCommands}",
                                   colour=colour_choice,
                                   timestamp=datetime.utcnow())
                adminEmbed.set_footer(
                    text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
                await act.send(embed=adminEmbed)

            elif group == 'Embeds' or group == 'embeds':
                rulesChannel: TextChannel = self.client.get_channel(
                    926018106181185596)
                memberChannel: TextChannel = self.client.get_channel(
                    926018111285624932)
                embedCommands = f"**Rules**: Enter /rules to send the rules listed in {rulesChannel.mention}.\n\n" \
                    f"**Member List**: Enter /members to send the member list listed in {
                        memberChannel.mention}."
                embedsEmbed = Embed(title="**__Embed Commands__**",
                                    description=f">>> {embedCommands}",
                                    colour=colour_choice,
                                    timestamp=datetime.utcnow())
                embedsEmbed.set_footer(
                    text=f"/help {group}: {act.user.display_name}", icon_url=act.user.avatar.url)
                await act.send(embed=embedsEmbed)
            else:
                await act.send("No command category found with that name!")
        else:
            await act.send("You do not have permission to do that!\nTry /help instead.")


def setup(client: commands.Bot):
    client.add_cog(AdminHelpCommand(client))
