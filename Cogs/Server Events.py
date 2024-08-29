import random
import time
from datetime import datetime

import nextcord
from nextcord import *
from nextcord.ext import commands


class LeaveAndJoin(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        # Field One
        rulesChannel = self.client.get_channel(926018106181185596)
        reactionRolesChannel = self.client.get_channel(926018107884044338)
        generalChannel = self.client.get_channel(926018138141773864)
        clipsChannel = self.client.get_channel(926018115870031912)
        # Field Two
        saddusFeaturesChannel = self.client.get_channel(963798521511821332)
        sicariusSocialsChannel = self.client.get_channel(955573761900441600)

        user = member
        if user.bot:
            pass
        else:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)
            doorway_channel = self.client.get_channel(926018092931379240)
            doorway_embed = Embed(title="≾ Doorway to ꜱɪᴄᴀʀɪᴜꜱ ≿",
                                  description=f"Welcome, **{member.name}#{
                                      member.discriminator}**!\nMember Number *{member.guild.member_count}*",
                                  colour=colour_choice,
                                  timestamp=datetime.utcnow(),
                                  url="https://discord.gg/fN72Eh3tEw")
            doorway_embed.add_field(name="Things to do:", inline=False,
                                    value=f"⊜ Read the {rulesChannel.mention}.\n⊜ Get some {reactionRolesChannel.mention}.\n⊜ Have a chat in {generalChannel.mention}.\n⊜ Check out some {clipsChannel.mention}.\n⊜ Check out our custom bot: {saddusFeaturesChannel.mention}.\n⊜ Check out Sicarius' socials in {sicariusSocialsChannel.mention}.")
            if member.avatar is None:
                pass
            else:
                doorway_embed.set_thumbnail(url=member.avatar.url)
            doorway_embed.set_footer(
                text="ꜱɪᴄᴀʀɪᴜꜱ Discord Server", icon_url=member.guild.icon.url)
            await doorway_channel.send(f"{member.mention}", embed=doorway_embed)
            # Member Counter
            time.sleep(1)
            member_counter = member.guild.stage_channels[0]
            await member_counter.delete()
            await member.guild.create_stage_channel(name=f'ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ: {member.guild.member_count}',
                                                    topic="Member Counter")
            default_role = member.guild.default_role
            channel_new = member.guild.stage_channels[0]
            await channel_new.set_permissions(default_role, connect=False)
            # Role Additions
            device_role = member.guild.get_role(927332770735329350)
            serverRelated_role = member.guild.get_role(927333218368237590)
            defaultColour_role = member.guild.get_role(928629266340519976)
            member_role = member.guild.get_role(926018077265641522)
            await member.add_roles(device_role, serverRelated_role, defaultColour_role, member_role)

    @commands.Cog.listener()
    async def on_member_remove(self, member: nextcord.Member):
        user = member
        if user.bot:
            pass
        else:
            colours = [0xeb05e3, 0x05bdeb]
            colour_choice = random.choice(colours)
            doorway_channel = self.client.get_channel(926018092931379240)
            doorway_embed = Embed(title="≾ Doorway to ꜱɪᴄᴀʀɪᴜꜱ ≿",
                                  description=f"So long, {member.name}.",
                                  colour=colour_choice,
                                  timestamp=datetime.utcnow())
            if member.avatar is None:
                pass
            else:
                doorway_embed.set_thumbnail(url=member.avatar.url)
            doorway_embed.set_footer(
                text="ꜱɪᴄᴀʀɪᴜꜱ Discord Server", icon_url=member.guild.icon.url)
            await doorway_channel.send(embed=doorway_embed)
            # Member Counter
            time.sleep(1)
            member_counter = member.guild.stage_channels[0]
            await member_counter.delete()
            await member.guild.create_stage_channel(name=f'ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ: {member.guild.member_count}',
                                                    topic="Member Counter")
            default_role = member.guild.default_role
            channel_new = member.guild.stage_channels[0]
            await channel_new.set_permissions(default_role, connect=False)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        colours = [0xeb05e3, 0x05bdeb]
        emoji = self.client.get_emoji(957303773729021972)
        if message.type == MessageType.premium_guild_subscription:
            boost_channel = self.client.get_channel(932294232587251804)
            embed = Embed(title="Server Boost Status",
                          description=f"{emoji} {
                              message.author.mention} just boosted the serer!\n"
                          f"{message.guild.name} has {
                              message.guild.premium_subscription_count} boosts!",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            embed.set_footer(text="ꜱɪᴄᴀʀɪᴜꜱ Boost Status",
                             icon_url=message.guild.icon.url)
            embed.set_thumbnail(url=message.author.display_avatar.url)
            await boost_channel.send(embed=embed)
        elif message.type == MessageType.premium_guild_tier_1:
            boost_channel = self.client.get_channel(932294232587251804)
            embed = Embed(title="Server Boost Status",
                          description=f"{emoji} {
                              message.author.mention} just boosted the serer!\n"
                          f"{message.guild.name} has {
                              message.guild.premium_subscription_count} boosts!\n"
                          f"{message.guild.name} has achieved Boost Tier 1",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            embed.set_footer(text="ꜱɪᴄᴀʀɪᴜꜱ Boost Status",
                             icon_url=message.guild.icon.url)
            embed.set_thumbnail(url=message.author.display_avatar.url)
            await boost_channel.send(embed=embed)

        elif message.type == MessageType.premium_guild_tier_2:
            boost_channel = self.client.get_channel(932294232587251804)
            embed = Embed(title="Server Boost Status",
                          description=f"{emoji} {
                              message.author.mention} just boosted the serer!\n"
                          f"{message.guild.name} has {
                              message.guild.premium_subscription_count} boosts!\n"
                          f"{message.guild.name} has achieved Boost Tier 2",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            embed.set_footer(text="ꜱɪᴄᴀʀɪᴜꜱ Boost Status",
                             icon_url=message.guild.icon.url)
            embed.set_thumbnail(url=message.author.display_avatar.url)
            await boost_channel.send(embed=embed)

        elif message.type == MessageType.premium_guild_tier_3:
            boost_channel = self.client.get_channel(932294232587251804)
            embed = Embed(title="Server Boost Status",
                          description=f"{emoji} {
                              message.author.mention} just boosted the serer!\n"
                          f"{message.guild.name} has {
                              message.guild.premium_subscription_count} boosts!\n"
                          f"{message.guild.name} has achieved Boost Tier 3",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            embed.set_footer(text="ꜱɪᴄᴀʀɪᴜꜱ Boost Status",
                             icon_url=message.guild.icon.url)
            embed.set_thumbnail(url=message.author.display_avatar.url)
            await boost_channel.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if not message.author.bot:
            if message.attachments:
                if random.randint(1, 2) == 1:
                    await message.add_reaction("⭐")
        else:
            pass


def setup(client: commands.Bot):
    client.add_cog(LeaveAndJoin(client))
