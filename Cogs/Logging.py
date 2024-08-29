import datetime

import nextcord
from nextcord import *
from nextcord.ext import commands


class Logging(commands.Cog, name="Logging"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            pass
        else:
            author, content = message.author, message.content
            channel: TextChannel = message.channel
            if not channel == self.client.get_channel(931814532341448754):
                logChannel = self.client.get_channel(955776300776300594)
                embed = Embed(title="Message Deleted",
                              description=f"Author: {author}\n"
                              f"Content: {content}\n"
                              f"Channel: {channel}\n"
                              f"Time: {datetime.datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
                await logChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot or after.author.bot:
            pass
        else:
            author, discriminator = before.author.name, before.author.discriminator
            logChannel = self.client.get_channel(955776300776300594)
            embed = Embed(title="Message Edited",
                          description=f"Author: {
                              author}\nContent Before: {before.content}\n"
                          f"Content After: {after.content}\n"
                          f"Channel: {before.channel}\n"
                          f"Time: {datetime.datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
            await logChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        logChannel = self.client.get_channel(955776300776300594)
        embed = Embed(title="Member Joined",
                      description=f"Name: {member.name}{
                          member.discriminator}.\n"
                      f"Time: {datetime.datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
        await logChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, user: nextcord.User):
        logChannel = self.client.get_channel(955776300776300594)
        embed = Embed(title="User Left",
                      description=f"Name: {user.name}{user.discriminator}.\n"
                      f"Time: {datetime.datetime.utcnow().strftime(f'%y/%m/%d at %H:%M')}")
        await logChannel.send(embed=embed)


"""
    @commands.Cog.listener()
    async def on_member_ban(self, user: nextcord.User):
        logChannel = self.client.get_channel(955776300776300594)
        embed = Embed(title="Member Banned",
                      description=f"Member: {user.name}#{user.discriminator}")
        await logChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, user: nextcord.User):
        logChannel = self.client.get_channel(955776300776300594)
        embed = Embed(title="User Unbanned",
                      description=f"Author: {user.name}{user.discriminator}")
        await logChannel.send(embed=embed)
"""


def setup(client: commands.Bot):
    client.add_cog(Logging(client))
