from nextcord.ext import commands


class EventHandlers(commands.Cog, name="Event Handlers"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(
                f"You are missing the required parameters for that command.\nYour required parameter: **{error.param.name}**\n\nType "f"s-help for more information.")

        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("That command does not exist!\n\nType s-help for more information.")

        elif isinstance(error, commands.errors.UserNotFound):
            await ctx.send(
                "That user does not exist.\nPlease try mentioning another user.\n\nType s-help for more information.")

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(
                "That user does not exist.\nPlease try mentioning another user.\n\nType s-help for more information.")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"The counting must stop because I am on cooldown.\nTry again in {error.retry_after:.2f} seconds.")

        else:
            raise error


def setup(client: commands.Bot):
    client.add_cog(EventHandlers(client))
