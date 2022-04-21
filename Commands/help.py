import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(helpCog(bot))


class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(send_messages=True)
    async def help(self, ctx):
        embed = discord.Embed(title="HELP !", value="Need Help ?", color=0xDEFD00)
        embed.set_thumbnail(url="https://emoji.discord.st/emojis/9bc890f3-63ca-4a35-a672-788ccc69953e.webp")
        embed.add_field(name="``Admin commands``", value="Commands that can only be done by admins", inline=False)

        embed.add_field(name="``Prefix``", value="***The prefix of the bot*** "
                                                 "\nù", inline=False)

        embed.add_field(name="``ùban``", value="***Ban a member*** "
                                               "\nùban [member-mention] ([raison])", inline=True)
        embed.add_field(name="``ùunban``", value="***Unban a member*** "
                                                 "\nùunban [username#usertag]", inline=True)
        embed.add_field(name="``ùtempBan``", value="***Ban a member for the defined duration*** "
                                                   "\nùtempBan [member-mention] [duration] ([raison])", inline=True)

        embed.add_field(name="``ùmute``", value="***The designated member will no longer be able to speak*** "
                                                "\nùmute [member-mention] ([raison])", inline=True)
        embed.add_field(name="``ùunmute``", value="***The designated member will be able to speak again*** "
                                                  "\nùunmute [member-mention]", inline=True)
        embed.add_field(name="``ùtempMute``", value="***Mute a member for the defined duration*** "
                                                    "\nùtempMute [member-mention] [duration] ([raison])", inline=True)

        embed.add_field(name="``ùvisit``", value="***Get the visit role for speak with the prisoner (the muted)*** "
                                                 "\nùvisit", inline=False)
        embed.add_field(name="``ùkick``", value="***Expel the designated member from the server "
                                                "(he can come back with an invitation)*** "
                                                "\nùkick [member-mention] ([raison])", inline=False)

        embed.add_field(name="``ùclear``", value="***Delete the number of messages indicated*** "
                                                 "\nùclear [number-of-messages]", inline=True)
        embed.add_field(name="``ùclearAll``", value="***Delete all messages from the channel*** "
                                                    "\nùclearAll", inline=True)

        embed.add_field(name="``ùJudgement``", value="***Randomly selects a sanction between "
                                                     "\"Ban\", \"Temp Ban\", \"Kick\", \"Mute\", \"Slave role\". "
                                                     "Leave one minute before the application of the selected sanction."
                                                     "Applies the penalty automatically.*** "
                                                     "\nùJudgement [member-mention] ([raison]) "
                                                     "\n**Warning! You cannot reverse the sanction. "
                                                     "You must ask @Dreyse to process.**", inline=False)
        await ctx.send(embed=embed)
