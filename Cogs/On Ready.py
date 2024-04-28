import nextcord
from nextcord.ext import commands


class OnReady(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            status=nextcord.Status.dnd,
            activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="ꜱɪᴄᴀʀɪᴜꜱ"))
        bot_logs_channel = self.client.get_channel(932655328359743548)
        await bot_logs_channel.send("Online")
        print("Online")


def setup(client: commands.Bot):
    client.add_cog(OnReady(client))
