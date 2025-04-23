import nextcord
from nextcord import *
from nextcord.ext import commands
from wavelink import *
import datetime


class MusicControllers(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description='Play a song',
                            guild_ids=serverID)
    async def play(self,
                   act: Interaction, search: str = SlashOption(description="Song Name", required=True)):
        await act.response.defer()
        song = await YouTubeTrack.search(query=search, return_first=True)
        if not getattr(act.user.voice, 'channel', None):
            return await act.followup.send("You need to be in a voice channel to play music!")
        elif not act.guild.voice_client:
            vc: Player = await act.user.voice.channel.connect(cls=Player)
        else:
            vc: Player = act.guild.voice_client
        if not vc.is_playing() and vc.queue.is_empty:
            await vc.play(song)
            await vc.set_volume(10)
            embed = Embed(
                title="🔊 Now Playing:",
                description=f"`{song.title}`\nby: `{
                    song.author}`\nDuration: **{str(datetime.timedelta(seconds=song.length))}**",
                url=song.uri,
                colour=0x05bdeb)
            embed.set_thumbnail(url=song.thumb)
            embed.set_author(
                name='Saddu Music Utilities',
                icon_url="https://cdn.discordapp.com/attachments/945255580778500130/960114777873592350/dj-mix.gif")
            embed.set_footer(text=f"Requested by {act.user.display_name}#{
                             act.user.discriminator}", icon_url=act.user.display_avatar.url)
            await act.followup.send(embed=embed)
        elif vc.is_playing():
            await vc.queue.put_wait(song)
            embed = Embed(title=f"📜 Queue",
                          description=f"Added `{song.title}`\nby `{
                              song.author}` to the queue.",
                          colour=0x05bdeb)
            embed.set_thumbnail(url=song.thumb)
            embed.set_author(
                name=f"Saddu Music Utilities",
                icon_url="https://cdn.discordapp.com/attachments/945255580778500130/960114777873592350/dj-mix.gif")
            embed.set_footer(text=f"Queued by {act.user.display_name}#{
                             act.user.discriminator}", icon_url=act.user.avatar.url)
            await act.followup.send(embed=embed)

    @nextcord.slash_command(description='Pause any playing music',
                            guild_ids=serverID)
    async def pause(self, act: Interaction):
        if not act.guild.voice_client:
            return await act.channel.send("There is no music playing.\nUse /play to queue a track!", delete_after=5)
        elif not getattr(act.user.voice, 'channel', None):
            return await act.channel.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to pause music", delete_after=5)
        else:
            vc: Player = act.guild.voice_client
        await vc.pause()
        await act.send(f"Paused the music ⏸")

    @nextcord.slash_command(description='Resume the paused music',
                            guild_ids=serverID)
    async def resume(self, act: Interaction):
        if not act.guild.voice_client:
            return await act.channel.send("There is no music playing.\nUse /play to queue a track!", delete_after=5)
        elif not getattr(act.user.voice, 'channel', None):
            return await act.channel.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to resume the music", delete_after=5)
        else:
            vc: Player = act.guild.voice_client
        await vc.resume()
        emoji = self.client.get_emoji(960114684047032350)
        await act.send(f"▶ Resumed the music")

    @nextcord.slash_command(description='Stops any playing music',
                            guild_ids=serverID)
    async def stop(self,
                   act: Interaction,
                   dc: str = SlashOption(
                       description="'y' to disconnect the bot OR 'n' to not disconnect the bot",
                       required=False)):
        if not act.guild.voice_client:
            return await act.channel.send("There is no music playing.\nUse /play to queue a track!", delete_after=5)
        elif not getattr(act.user.voice, 'channel', None):
            return await act.channel.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to stop the music", delete_after=5)
        else:
            vc: Player = act.guild.voice_client
        await vc.stop()
        await act.send(f"Stopped the music ❌")
        if dc == "y":
            await vc.disconnect()

    @nextcord.slash_command(description="Changes the volume of the music",
                            guild_ids=serverID)
    async def volume(self,
                     act: Interaction,
                     amount: int = SlashOption(required=True, description="Changes the volume to the given amount. Recommended amount is 10")):
        if not act.guild.voice_client:
            return await act.channel.send("There is no music playing.\nUse /play to play a track!", delete_after=5)
        elif not getattr(act.user.voice, 'channel', None):
            return await act.channel.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to change the volume of your music", delete_after=5)
        else:
            vc: Player = act.guild.voice_client
        if amount > 100:
            amount = 100
            await act.channel.send("That amount is too high!", delete_after=5)
        elif amount < 0:
            amount = 1
        await vc.set_volume(amount)
        await act.send(f"Set the volume to {amount}% :speaker:")

    @nextcord.slash_command(description="Returns the music that is currently playing",
                            guild_ids=serverID)
    async def nowplaying(self, act: Interaction):
        if not act.guild.voice_client:
            return await act.send("There is no music playing.\nUse /play to play a track!", delete_after=5)
        elif not getattr(act.user.voice, 'channel', None):
            return await act.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to see whats playing", delete_after=5)
        else:
            vc: Player = act.guild.voice_client
        if not vc.is_playing():
            return await act.send("No music playing.\nUse /play to play a track!", delete_after=5)
        song = vc.track
        embed = Embed(
            title="🔊 Now Playing:",
            description=f"`{song.title}`\nby: `{
                song.author}`\nDuration: **{str(datetime.timedelta(seconds=song.length))}**",
            url=song.uri,
            colour=0x05bdeb)
        embed.set_thumbnail(url=song.thumb)
        embed.set_author(
            name='Saddu Music Utilities',
            icon_url="https://cdn.discordapp.com/attachments/945255580778500130/960114777873592350/dj-mix.gif")
        await act.send(embed=embed)


def setup(client):
    client.add_cog(MusicControllers(client))
