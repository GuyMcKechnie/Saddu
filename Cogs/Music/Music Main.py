import wavelink
import datetime
from wavelink import *
from nextcord import *
from nextcord.ext import commands


class MusicMain(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.loop.create_task(self.node_connect())

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready")

    serverID = [909525005694562384, 945255580778500127]

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f"Node Ready.\nID: {node.identifier}")

    async def node_connect(self):
        await self.client.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.client,
                                            host='lavalinkinc.ml',
                                            port=443,
                                            password='incognito',
                                            https=True,
                                            spotify_client=spotify.SpotifyClient(
                                                client_id="4ac64ce49bf74f35bd9b0c3f4003eb2e",
                                                client_secret="0cd40be4dfc4456b8f09f197e40ed9c4"))

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: Player, track, reason):
        channel = self.client.get_channel(926018139056128080)
        vc: player = player.guild.voice_client
        try:
            nextSong = vc.queue.get()
            await vc.play(nextSong)
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
            await channel.send(embed=embed)
        except:
            await vc.stop()
            print("Stopped: Queue is empty.")


def setup(client: commands.Bot):
    client.add_cog(MusicMain(client))
