import time
import random
from datetime import datetime
import nextcord
from nextcord import *
from nextcord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(name="addrole_default",
                            description="Add default roles",
                            guild_ids=serverID)
    async def defaultRoleAdditions(self, interaction: nextcord.Interaction, member: nextcord.Member):
        if interaction.user.guild_permissions.administrator:
            user = member
            device_role = user.guild.get_role(927332770735329350)
            misc_role = user.guild.get_role(927332847264596038)
            serverRelated_role = user.guild.get_role(927333218368237590)
            defaultColour_role = user.guild.get_role(928629266340519976)
            member_role = user.guild.get_role(926018077265641522)
            await user.add_roles(device_role, misc_role, serverRelated_role, defaultColour_role, member_role)
            await interaction.response.send_message("Added roles successfully.")
        else:
            await interaction.response.send_message("No permissions!")

    @nextcord.slash_command(name="addrole_ctfmember", description="Add CTF member roles",
                            guild_ids=serverID)
    async def ctfRoleAdditions(self, interaction: nextcord.Interaction, member: nextcord.Member):
        if interaction.user.guild_permissions.administrator:
            user = member
            ctf_member = user.guild.get_role(930839051265802312)
            tier_4 = user.guild.get_role(930524466843373598)
            ctf_title = user.guild.get_role(930523984343203952)
            await user.add_roles(ctf_title, tier_4, ctf_member)
            await interaction.response.send_message("Added roles successfully.")
        else:
            await interaction.response.send_message("No permissions!")

    @nextcord.slash_command(name="addrole_bot", description="Add bot roles",
                            guild_ids=serverID)
    async def botRoleAdditions(self, interaction: nextcord.Interaction, member: nextcord.Member):
        if interaction.user.guild_permissions.administrator:
            user = member
            bot_team = user.guild.get_role(926018078016413736)
            await user.add_roles(bot_team)
            await interaction.response.send_message("Added roles successfully.")

            device_role = user.guild.get_role(927332770735329350)
            misc_role = user.guild.get_role(927332847264596038)
            serverRelated_role = user.guild.get_role(927333218368237590)
            defaultColour_role = user.guild.get_role(928629266340519976)
            member_role = user.guild.get_role(926018077265641522)
            await user.remove_roles(device_role, misc_role, serverRelated_role, defaultColour_role, member_role)
            await interaction.response.send_message("Removed roles successfully.")
        else:
            await interaction.response.send_message("No permissions!")

    @nextcord.slash_command(guild_ids=serverID)
    async def roles(self, act: Interaction, member: Member):
        print(member.roles)

    @nextcord.slash_command(description="Removes roles for a level reset.",
                            guild_ids=serverID)
    async def levelreset(self, act: Interaction):
        if act.user.guild_permissions.administrator:
            await act.response.defer()
            loggingChannel: TextChannel = self.client.get_channel(
                932655328359743548)
            response = await loggingChannel.send("Initiating Level Reset...")
            roleUpdateMember = await loggingChannel.send("Initiating...")

            lvl1 = act.guild.get_role(927374013624361030)
            lvl5 = act.guild.get_role(927374090426265630)
            lvl10 = act.guild.get_role(927374117211082783)
            lvl15 = act.guild.get_role(927374181765623859)
            lvl20 = act.guild.get_role(927374214669947000)
            lvl25 = act.guild.get_role(930387597920993281)
            lvl30 = act.guild.get_role(932651842700185671)
            lvl35 = act.guild.get_role(952536494415962184)
            lvl40 = act.guild.get_role(952536532105969664)

            for member in act.user.guild.members:
                if not member.bot:
                    levelRoles = [lvl1, lvl5, lvl10, lvl15,
                                  lvl20, lvl25, lvl30, lvl35, lvl40]
                    for role in levelRoles:
                        if role in member.roles:
                            await member.remove_roles(role)
                            await roleUpdateMember.edit(f"Updated {member.name}.  Removed {role}")

            await roleUpdateMember.delete()
            await response.edit("Complete!")
            await response.delete(delay=2)
            await act.followup.send("Updated Level Roles!")

    @nextcord.slash_command(name="update", description="Update server", guild_ids=serverID)
    async def serverUpdate(self, act: nextcord.Interaction):
        if act.user.guild_permissions.administrator:
            await act.response.defer()
            loggingChannel: TextChannel = self.client.get_channel(
                932655328359743548)
            response = await loggingChannel.send("Initiating Server Update...")

            # Member Counter Update
            await response.edit("Updating Member Counter")
            member_counter = act.user.guild.stage_channels[0]
            await member_counter.delete()
            await act.user.guild.create_stage_channel(name=f'ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ: {act.user.guild.member_count}',
                                                      topic="Member Counter")
            default_role = act.user.guild.default_role
            channel_new = act.user.guild.stage_channels[0]
            await channel_new.set_permissions(default_role, connect=False)

            # Member Role Update
            await response.edit("Updating Member Roles")
            roleUpdateMember = await loggingChannel.send("Initiating...")
            for member in act.user.guild.members:
                if not member.bot:
                    device_role = act.user.guild.get_role(927332770735329350)
                    serverRelated_role = act.user.guild.get_role(
                        927333218368237590)
                    defaultColour_role = act.user.guild.get_role(
                        928629266340519976)
                    member_role = act.user.guild.get_role(926018077265641522)
                    memberRoles = [device_role, serverRelated_role,
                                   defaultColour_role, member_role]
                    for role in memberRoles:
                        if not role in member.roles:
                            await member.add_roles(device_role, serverRelated_role, defaultColour_role, member_role)
                            await roleUpdateMember.edit(f"Updated {member.mention}.")
                    print(f"{member.name}#{member.discriminator} is up to date")
            await roleUpdateMember.delete()
            await response.edit("Updated Member Roles")

            # Bot Role Update
            await response.edit("Updating Bot Roles")
            for bot in act.user.guild.bots:
                botTeamRole = act.user.guild.get_role(926018078016413736)
                if not botTeamRole in bot.roles:
                    print(f"Updating roles for {bot.name}")
                    await bot.add_roles(botTeamRole)
                    roleUpdateBot = await loggingChannel.send(f"Updated {bot.name}.")
                # Member role remove from bot
                device_role = act.user.guild.get_role(927332770735329350)
                serverRelated_role = act.user.guild.get_role(
                    927333218368237590)
                defaultColour_role = act.user.guild.get_role(
                    928629266340519976)
                member_role = act.user.guild.get_role(926018077265641522)
                memberRoles = [device_role, serverRelated_role,
                               defaultColour_role, member_role]
                for role in memberRoles:
                    if role in bot.roles:
                        await bot.remove_roles(role)
                        print(f"Removed {role} from {bot.name}.")
                print(f"{bot.name}#{bot.discriminator} is up to date")
            await response.edit("Updated Bot Roles")

            # Invite Channel Update
            await response.edit("Updating Invite Information.")
            if act.guild.premium_tier == 3:
                inviteChannel: VoiceChannel = act.guild.voice_channels[0]
                await act.guild.edit(vanity_code="sicarius")
                await inviteChannel.edit(name=f"ᴅɪꜱᴄᴏʀᴅ.ɢɢ/ꜱɪᴄᴀʀɪᴜꜱ")
                print("Updated invite channel & vanity link\n")
            else:
                inviteChannel: VoiceChannel = act.guild.voice_channels[0]
                await inviteChannel.edit(name=f"discord.gg/fN72Eh3tEw")
                print("Updated invite channel\n")
            await response.edit("Updated Invite Information.")

            # End of update
            await response.delete(delay=2)
            await act.followup.send("Updated successfully!")

    @nextcord.slash_command(name="ban", description="Ban a member", guild_ids=serverID)
    async def banCommand(self, interaction: nextcord.Interaction,
                         member: nextcord.Member = nextcord.SlashOption(description="Ban a member using their @.",
                                                                        required=True),
                         reason: str = nextcord.SlashOption(description="Provide a reason for the ban.",
                                                            required=False)):
        if interaction.user.guild_permissions.administrator:
            if interaction.user.id == member.id:
                await interaction.response.send_message("Cannot ban yourself!")
            elif member == member.guild_permissions.administrator:
                await interaction.response.send_message("Cannot ban administrators!")
            else:
                if reason is None:
                    await member.ban(reason="No reason given.")
                    await interaction.response.send_message(
                        f"{member.name}#{member.discriminator} has been banned by {interaction.user.mention}.\nReason: No reason given.")
                else:
                    await member.ban(reason=reason)
                    await interaction.response.send_message(
                        f"{member.name}#{member.discriminator} has been banned by {interaction.user.mention}.\nReason: {reason}.")
        else:
            await interaction.response.send_message(f"You do not have permission to do this!")

    @nextcord.slash_command(name="unban", description="Ban a member", guild_ids=serverID)
    async def unban(self, interaction: nextcord.Interaction,
                    identity=nextcord.SlashOption(
                        description="Unban a user using their ID", required=True),
                    reason: str = nextcord.SlashOption(description="Provide a reason for the unban", required=False)):
        if interaction.user.guild_permissions.administrator:
            if reason is None:
                member = await self.client.fetch_user(identity)
                await interaction.guild.unban(member, reason="No reason given.")
                await interaction.response.send_message(
                    f"{identity} was successfully unbanned by {interaction.user.mention}.\nReason: No reason given.")
            else:
                member = await self.client.fetch_user(identity)
                await interaction.guild.unban(member, reason=reason)
                await interaction.response.send_message(
                    f"{identity} was successfully unbanned by {interaction.user.mention}.\nReason: {reason}.")
        else:
            await interaction.response.send_message(f"You do not have permission to do this!")

    @nextcord.slash_command(name="timeout", description="Time a member out", guild_ids=serverID)
    async def timeout(self, interaction: nextcord.Interaction,
                      member: nextcord.Member = nextcord.SlashOption(description="Mute a member using their @.",
                                                                     required=True),
                      days: int = nextcord.SlashOption(
                          description="Enter how many days to timeout", required=True),
                      hours: int = nextcord.SlashOption(
                          description="Enter how many hours to timeout", required=True),
                      minutes: int = nextcord.SlashOption(description="Enter how many minutes to timeout",
                                                          required=True),
                      seconds: int = nextcord.SlashOption(description="Enter how many seconds to timeout",
                                                          required=True),
                      reason: str = nextcord.SlashOption(description="Provide a reason for the time out",
                                                         required=False)):
        if interaction.user.guild_permissions.administrator:
            if member == member.guild_permissions.administrator:
                await interaction.response.send_message("You cannot time administrators out!")
            if interaction.user.id == member.id:
                await interaction.response.send_message("You cannot time yourself out!")
            else:
                if days is None:
                    var = days == 0
                if hours is None:
                    var = hours == 0
                if minutes is None:
                    var = minutes == 0
                if seconds is None:
                    var = seconds == 1

                duration = datetime.timedelta(
                    days=days, hours=hours, minutes=minutes, seconds=seconds)

                if reason is None:
                    await member.edit(nick=f"[Timed Out] {member.display_name}", timeout=duration)
                    await interaction.response.send_message(
                        f"{member.mention} has been timed out by {interaction.user.men} successfully!\nDuration: {duration}"
                        f"\nReason: No reason provided.\n")
                    # Logging
                    logChannel = self.client.get_channel(955776300776300594)
                    embed = Embed(title="Member Timed Out",
                                  description=f"Authorizer: {interaction.user.name}#{
                                      interaction.user.discriminator}.\n"
                                  f"Member: {member.name}#{member.discriminator}\nDuration:{duration}.")
                    await logChannel.send(embed=embed)

                else:
                    await member.edit(nick=f"[Timed Out] {member.display_name}", timeout=duration)
                    await interaction.response.send_message(
                        f"{member.mention} has been timed out by {interaction.user.mention} successfully!\nDuration: "
                        f"{duration}\nReason: {reason}.\n")
                    # Logging
                    logChannel = self.client.get_channel(955776300776300594)
                    embed = Embed(title="Member Timed Out",
                                  description=f"Authorizer: {interaction.user.name}#{
                                      interaction.user.discriminator}."
                                  f"\nMember: {member.name}#{member.discriminator}\nDuration:{duration}.")
                    await logChannel.send(embed=embed)
        else:
            await interaction.response.send_message("You do not have permission to do this!")

    @nextcord.slash_command(name="ttag", description="Remove timeout tag", guild_ids=serverID)
    async def ttag(self, interaction: nextcord.Interaction,
                   member: nextcord.Member = nextcord.SlashOption(
                       description="Remove the timeout tag from a member using their @",
                       required=True)):
        if interaction.user.guild_permissions.administrator:
            await member.edit(nick=member.name)
            await interaction.response.send_message(f"Removed the tag from {member.name} successfully!")
        else:
            await interaction.response.send_message("You do not have permission to do this!")

    @nextcord.slash_command(description="Nana's test command. Do not run without permission!",
                            guild_ids=serverID)
    async def test(self, act: Interaction, member: Member):
        print("Test")

    @nextcord.slash_command(name="delrole", description="Delete a role", guild_ids=serverID)
    async def delRole(self, act: Interaction, member: nextcord.Member):
        if act.user.guild_permissions.administrator:
            qRole = member.guild.get_role(958402876663820359)
            await member.remove_roles(qRole)

    @nextcord.slash_command(name="kick", description="Remove someone from the server. WARNING: OP", guild_ids=serverID)
    async def kick(self, act: Interaction, member: nextcord.Member):
        if act.user.guild_permissions.administrator:
            await member.kick()


def setup(client):
    client.add_cog(Admin(client))
