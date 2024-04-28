import nextcord, os, asyncio, ffmpeg, random, json
from nextcord import *
from nextcord.ext import commands
from datetime import datetime


class ControllersCounting(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
    serverID = [909525005694562384, 945255580778500127]
    
    @nextcord.slash_command(description="Returns the number that counting is currently on",
                            guild_ids=serverID)
    async def number(self, act: Interaction):
        f = open("/home/container/Cogs/Counting/CountingDatabase.json")
        updatedData = json.load(f)
        updatedNumber = int(updatedData[0])
        colours = [0xeb05e3, 0x05bdeb]
        embed = Embed(title="Sicarius Counting Machine 2000", 
                        description=f"The current count is {str(updatedNumber)}", 
                        colour=random.choice(colours),
                        timestamp=datetime.utcnow())
        await act.send(embed=embed)
        f.close()
    
    
def setup(client: commands.Bot):
    client.add_cog(ControllersCounting(client))