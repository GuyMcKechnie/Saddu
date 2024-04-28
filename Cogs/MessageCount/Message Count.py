import sqlite3, random
from datetime import datetime
import nextcord
from nextcord import *
from nextcord.ext import commands

serverID = [909525005694562384, 945255580778500127]


class MessageCount(commands.Cog, name="MessageCount Commands"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                pass
            else:
                amount = ""
                user_id = message.author.id
                # Database
                dbConnection = sqlite3.connect("/home/container/Cogs/MessageCount/messageCountDatabase.db")
                cursor = dbConnection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS messageCountDatabase
                            (id INT PRIMARY KEY, 
                            messageNumber INTEGER SECONDARY KEY)""")
                cursor.execute("""INSERT OR IGNORE INTO messageCountDatabase VALUES
                            (?, 0)""", (user_id,))
                dbConnection.commit()
                for row in cursor.execute("""SELECT messageNumber FROM messageCountDatabase WHERE id = ?""", (user_id,)):
                    amount = row
                listOfMessageNumber = list(amount)
                listOfMessageNumber[0] += 1
                cursor.execute("""UPDATE messageCountDatabase SET messageNumber = ? WHERE id = ?""",
                            (listOfMessageNumber[0], user_id,))
                dbConnection.commit()
                # Database
        except sqlite3.OperationalError:
            pass

    @nextcord.slash_command(description="Returns the amount of messages by the user",
                            guild_ids=serverID)
    async def count(self, act: Interaction, member: nextcord.Member = SlashOption(required=True)):
        await act.response.defer()
        amount = ""
        # Database
        connection = sqlite3.connect("/home/container/Cogs/MessageCount/messageCountDatabase.db")
        cursor = connection.cursor()
        for row in cursor.execute("""SELECT messageNumber FROM messageCountDatabase WHERE id = ?""", (member.id,)):
            amount = row
        # Database
        if not list(amount):
            await act.followup.send(f"{member.name} does not have any messages in the server!", delete_after=10)
        else:
            colours = [0xeb05e3, 0x05bdeb]
            listAmount = list(amount)
            embed = Embed(title=f"{member.name}'s Message Count",
                          description=f"#{listAmount[0]}",
                          timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            await act.followup.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        try:
            amount = ""
            user_id = message.author.id
            # Database
            dbConnection = sqlite3.connect("/home/container/Cogs/MessageCount/serverMessageCountDatabase.db")
            cursor = dbConnection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS messageCountDatabase
                        (messageNumber INT PRIMARY KEY)""")
            for row in cursor.execute("""SELECT messageNumber FROM messageCountDatabase"""):
                amount = row
            listOfMessageNumber = list(amount)
            x = listOfMessageNumber[0] + 1
            cursor.execute("""INSERT OR IGNORE INTO messageCountDatabase VALUES(?)""", (x,))
            dbConnection.commit()
            for row in cursor.execute("""SELECT messageNumber FROM messageCountDatabase"""):
                amount = row
            listOfMessageNumber = list(amount)
            x = listOfMessageNumber[0] + 1
            cursor.execute("""UPDATE messageCountDatabase SET messageNumber = ?""", (x,)) 
            dbConnection.commit()
            # Database
        except sqlite3.OperationalError:
            pass
        
    @nextcord.slash_command(description="Returns the server's message count",
                            guild_ids=serverID)
    async def scount(self, act: Interaction):
        colours = [0xeb05e3, 0x05bdeb]
        await act.response.defer()
        amount = ""
        # Database
        connection = sqlite3.connect("/home/container/Cogs/MessageCount/serverMessageCountDatabase.db")
        cursor = connection.cursor()
        for row in cursor.execute("""SELECT messageNumber FROM messageCountDatabase"""):
            amount = row
        # Database
        if not list(amount):
            await act.followup.send(f"There are no messages in this server!")
        else:
            listAmount = list(amount)
            embed = Embed(title="Server Message Counter", 
                          description=f"{act.guild.name}'s amount of messages: {listAmount[0]}", 
                          colour=random.choice(colours), 
                          timestamp=datetime.utcnow())
            await act.followup.send(embed=embed) 


def setup(client: commands.Bot):
    client.add_cog(MessageCount(client))
