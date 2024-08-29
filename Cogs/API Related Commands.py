import io
import random

import aiohttp
import nextcord
import requests
from nextcord import *
from nextcord.ext import commands

serverID = [909525005694562384, 945255580778500127]


class APICommands(commands.Cog, name="API Commands"):
    def __init__(self, client: commands.Bot):
        self.client = client

    serverID = [909525005694562384, 945255580778500127]

    @nextcord.slash_command(description="Overlay a members avatar with a horny overlay",
                            guild_ids=serverID)
    async def horny(self, intact: Interaction,
                    member: Member = SlashOption(
                        description="Enter a name of the user you want to apply the overlay to",
                        required=True)):
        colours = [0xeb05e3, 0x05bdeb]
        colour_choice = random.choice(colours)
        avatar = member.avatar.url
        await intact.send("Making your poster!")
        await intact.user.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://some-random-api.ml/canvas/horny?avatar={avatar}') as image:
                if 300 > image.status >= 200:
                    f = io.BytesIO(await image.read())
                    file = nextcord.File(f, "horny.png")
                    horny_embed = Embed(title="Someone's Horny",
                                        colour=colour_choice)
                    horny_embed.set_image(url="attachment://horny.png")
                    await intact.send(embed=horny_embed, file=file)
                else:
                    await intact.send("Don't be horny!")
                await session.close()

    @nextcord.slash_command(description="Sends a random funny joke",
                            guild_ids=serverID)
    async def joke(self, intact: Interaction):
        joke_request = requests.get("https://some-random-api.ml/joke")
        if 300 > joke_request.status_code >= 200:
            content = joke_request.json()
        else:
            content = "Received bad requests"
        await intact.send(content["joke"])
        fetchedEmoji = self.client.get_emoji(919321967465750578)
        await intact.channel.send(fetchedEmoji)

    @nextcord.slash_command(description="Sends an inspirational quote",
                            guild_ids=serverID)
    async def quote(self, intact: Interaction):
        quote_request = requests.get("https://zenquotes.io/api/random/")
        if 300 > quote_request.status_code >= 200:
            content = quote_request.json()
        else:
            content = "Received bad requests"
        contentA = content[0]
        await intact.send(contentA['q'])


def setup(client: commands.Bot):
    client.add_cog(APICommands(client))
