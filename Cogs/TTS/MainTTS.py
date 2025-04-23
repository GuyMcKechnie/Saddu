from datetime import datetime
import random 
import nextcord
import asyncio
from gtts import gTTS
from nextcord import *
from nextcord.ext import commands


class TTS(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    def audio_len(path):
        global MP3
        audio = MP3(path)
        return (audio.info.length)

    @nextcord.slash_command(description="TTS module for sending TTS messages in a voice channel",
                            guild_ids=serverID)
    async def tts(self, act: Interaction, *, message: str = SlashOption(required=True, description="Message to send with TTS")):
        global gTTS
        colours = [0xeb05e3, 0x05bdeb]
        speech = gTTS(text=message, lang='en', slow=False)
        speech.save("audio.mp3")

        if not getattr(act.user.voice, 'channel', None):
            return await act.send(
                "You are not in a Voice Channel.\nPlease join a voice channel to use the TTS functions!", delete_after=5)
        elif not act.guild.voice_client:
            vc = await act.user.voice.channel.connect()
            embed = Embed(title="Joining Voice Channel.",
                          description="",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            await act.send(embed=embed, delete_after=5)
        else:
            vc = act.guild.voice_client

        vc.play(FFmpegPCMAudio(source="/home/container/audio.mp3"))
        embed = Embed(title="TTS by Saddu",
                      description=f"{act.user.display_name} says\n`{message}`",
                      colour=random.choice(colours),
                      timestamp=datetime.utcnow())
        embed.set_thumbnail(url=act.user.avatar.url)
        await act.send(embed=embed)
        await asyncio.sleep(300)
        await vc.disconnect(force=True)


def setup(client: commands.Bot):
    client.add_cog(TTS(client))
