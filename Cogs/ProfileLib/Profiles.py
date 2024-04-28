import random
from datetime import datetime, timezone
from io import BytesIO

import nextcord
from PIL import Image, ImageChops, ImageDraw, ImageFont
from nextcord import *
from nextcord.ext import commands

serverID = [909525005694562384, 945255580778500127]


def circle(pfp, size=(145, 145)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

    bigSize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigSize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigSize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


class Profiles(commands.Cog, name="Profile Commands"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @nextcord.slash_command(description="Returns the user's avatar or profile image",
                            guild_ids=serverID)
    async def avatar(self, act: Interaction, member: nextcord.Member = SlashOption(required=True)):
        colours = [0xeb05e3, 0x05bdeb]
        emoji = self.client.get_emoji(959776440373633054)
        loading = await act.channel.send(f"Fetching {member.name}'s avatar {emoji}")
        await act.response.defer()
        if member.avatar is None:
            await loading.edit(f"{member.name} does not have an avatar!")
        else:
            embed = Embed(title=f"{member.name}'s Avatar", description="", timestamp=datetime.utcnow(),
                          colour=random.choice(colours))
            embed.set_image(url=member.avatar.url)
            await act.followup.send(embed=embed)
            await loading.edit(f"Created {member.name}'s avatar successfully", delete_after=2)

    @nextcord.slash_command(description="Returns a summary of the server",
                            guild_ids=serverID)
    async def server(self, act: Interaction):
        emoji = self.client.get_emoji(959776440373633054)
        loading = await act.channel.send(f"Creating {act.guild.name}'s user profile. {emoji}")
        await act.response.defer()
        colours = [0xeb05e3, 0x05bdeb]

        server_embed = Embed(title=f"{act.guild.name} Server Profile", description="", colour=random.choice(colours),
                             timestamp=datetime.utcnow())

        ownerE = self.client.get_emoji(959779101785354280)
        server_embed.add_field(name=f"{ownerE} Server Owner",
                               value=f"{act.guild.owner}\n"
                                     f"**Server Description**\n"
                                     f"{act.guild.description}",
                               inline=False)

        boostE = self.client.get_emoji(959779367431598151)
        server_embed.add_field(name=f"{boostE} Boost Status",
                               value=f"Level: {act.guild.premium_tier}\n"
                                     f"Boosts: {act.guild.premium_subscription_count}",
                               inline=False)

        memberE = self.client.get_emoji(959779663264223262)
        botCount = 0
        for bot in act.guild.bots:
            botCount += 1
        server_embed.add_field(name=f"{memberE} Member Summary",
                               value=f"> Total Members: {act.guild.member_count}\n"
                                     f">  Bot Members: {botCount}\n"
                                     f">  Human Members: {act.guild.member_count - botCount}",
                               inline=True)

        channelE = self.client.get_emoji(959780921593188402)
        b, c, d, e = 0, 0, 0, 0
        for channel in act.guild.channels:
            b += 1
        for channel in act.guild.text_channels:
            c += 1
        for channel in act.guild.voice_channels:
            d += 1
        for channel in act.guild.stage_channels:
            e = + 1
        server_embed.add_field(name=f"{channelE} Channel Summary",
                               value=f"> Total Channels: {b}\n"
                                     f">  Text Channels: {c}\n"
                                     f">  Voice Channels: {d}\n"
                                     f">  Stage Channels: {e}",
                               inline=True)

        calE = self.client.get_emoji(959781236040138824)
        creation_date = str(act.guild.created_at)
        creation_date_split = creation_date.split(" ")
        server_embed.add_field(name=f"{calE} Creation Date",
                               value=creation_date_split[0],
                               inline=False)
        age = act.guild.created_at - datetime.now(timezone.utc)
        age = age.days
        server_embed.add_field(name=f"{calE} Age",
                               value=f"{(-1 * age)} days",
                               inline=True)

        emojiE = self.client.get_emoji(959782154462724098)
        a = 0
        for emoji in act.guild.emojis:
            a += 1
        server_embed.add_field(name=f"{emojiE} Total Emojis ",
                               value=f"{a}",
                               inline=False)

        rolE = self.client.get_emoji(959787745654501406)
        f = 0
        for role in act.guild.roles:
            f += 1
        server_embed.add_field(name=f"{rolE} Total Roles",
                               value=f"{f}",
                               inline=True)

        server_image = act.guild.icon.url
        server_embed.set_thumbnail(url=server_image)
        server_embed.set_footer(text=f"Server ID: {act.guild.id}", icon_url=server_image)

        await act.followup.send(embed=server_embed)
        await loading.edit("Created server profile successfully!", delete_after=2)

    @nextcord.slash_command(description="Returns a detailed profile summary about a user",
                            guild_ids=serverID)
    async def profile(self,
                      act: Interaction,
                      member: nextcord.Member = SlashOption(required=True, description="Enter the member name")):

        global memberProfilePicture, pfp

        emoji = self.client.get_emoji(959776440373633054)
        loading = await act.channel.send(f"Creating {member.name}'s user profile {emoji}")
        await act.response.defer()

        name, nick, Id = str(f"{member.name}#{member.discriminator}").upper(), f"AKA {member.display_name}", str(
            member.id)
        status, botUser = str(member.status).upper(), str(member.bot)
        created_at = member.created_at.strftime("%a %b %Y")
        joined_at = member.joined_at.strftime("%a %b %Y")

        base = Image.open("Cogs/ProfileLib/Profile-Image.png").convert("RGBA")

        if () == member.activities:
            activity = None
        else:
            activity = str(member.activities[0].name)

        if member.avatar is None:
            pass
        else:
            memberProfilePicture = member.avatar
            data = BytesIO(await memberProfilePicture.read())
            memberProfilePicture = Image.open(data).convert("RGBA")

        name = f"{name[:14]}.." if len(name) > 14 else name
        nick = f"{nick[:32]}.." if len(nick) > 32 else nick

        if activity is None:
            pass
        else:
            activity = f"{activity[:24]}.." if len(activity) > 24 else activity

        draw = ImageDraw.Draw(base)
        if member.avatar is None:
            pass
        else:
            pfp = circle(memberProfilePicture, (145, 145))
        font = ImageFont.truetype("Cogs/ProfileLib/Profile-Font.otf", 40)
        nickFont = ImageFont.truetype("Cogs/ProfileLib/Profile-Font.otf", 20)
        subFont = ImageFont.truetype("Cogs/ProfileLib/Profile-Font.otf", 17)

        draw.text((190, 83), name, font=font)
        if nick is None:
            pass
        else:
            draw.text((190, 137), nick, font=nickFont)
        draw.text((53, 263), botUser, font=subFont)
        if activity is None:
            draw.text((53, 333), "None", font=subFont)
        else:
            draw.text((53, 333), activity, font=subFont)
        draw.text((325, 263), Id, font=subFont)
        draw.text((325, 333), status, font=subFont)
        draw.text((53, 403), joined_at, font=subFont)
        draw.text((325, 403), created_at, font=subFont)

        if member.avatar is None:
            pass
        else:
            base.paste(pfp, (39, 37), pfp)

        with BytesIO() as a:
            base.save(a, "PNG")
            a.seek(0)
            await act.followup.send(file=File(a, "Profile.png"))

        await loading.edit(f"Created {member.display_name}'s profile successfully!", delete_after=2)


def setup(client: commands.Bot):
    client.add_cog(Profiles(client))
