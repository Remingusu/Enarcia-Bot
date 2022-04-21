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
        sembed = discord.Embed(title="HELP !", value="Need Help ?", color=0xDEFD00)
        sembed.set_thumbnail(url="https://ibb.co/L8PmYCL")
        sembed.add_field(name="``Prefix``", value="***The prefix of the bot*** "
                                                  "\nù", inline=False)
        sembed.add_field(name="Summary", value="1. Admin commands "
                                               "\n 2. Other commands", inline=False)

        aembed = discord.Embed(title="Admin Help !", value="List of commands for admin / modo", color=0xD70000)
        aembed.set_thumbnail(url="https://ibb.co/X4Rv6LB")
        aembed.add_field(name="``ùban``", value="***Ban a member*** "
                                                "\nùban [member-mention] ([raison])", inline=True)
        aembed.add_field(name="``ùunban``", value="***Unban a member*** "
                                                  "\nùunban [username#usertag]", inline=True)
        aembed.add_field(name="``ùtempBan``", value="***Ban a member for the defined duration*** "
                                                    "\nùtempBan [member-mention] [duration] ([raison])", inline=True)

        aembed.add_field(name="``ùmute``", value="***The designated member will no longer be able to speak*** "
                                                 "\nùmute [member-mention] ([raison])", inline=True)
        aembed.add_field(name="``ùunmute``", value="***The designated member will be able to speak again*** "
                                                   "\nùunmute [member-mention]", inline=True)
        aembed.add_field(name="``ùtempMute``", value="***Mute a member for the defined duration*** "
                                                     "\nùtempMute [member-mention] [duration] ([raison])", inline=True)

        aembed.add_field(name="``ùvisit``", value="***Get the visit role for speak with the prisoner (the muted)*** "
                                                  "\nùvisit", inline=False)
        aembed.add_field(name="``ùkick``", value="***Expel the designated member from the server "
                                                 "(he can come back with an invitation)*** "
                                                 "\nùkick [member-mention] ([raison])", inline=False)

        aembed.add_field(name="``ùclear``", value="***Delete the number of messages indicated*** "
                                                  "\nùclear [number-of-messages]", inline=True)
        aembed.add_field(name="``ùclearAll``", value="***Delete all messages from the channel*** "
                                                     "\nùclearAll", inline=True)

        aembed.add_field(name="``ùJudgement``", value="***Randomly selects a sanction between "
                                                      "\"Ban\", \"Temp Ban\", \"Kick\", \"Mute\", \"Slave role\". "
                                                      "Leave one minute before the application of the selected sanction."
                                                      "Applies the penalty automatically.*** "
                                                      "\nùJudgement [member-mention] ([raison]) "
                                                      "\n**Warning! You cannot reverse the sanction. "
                                                      "You must ask @Dreyse to process.** "
                                                      "\n", inline=False)

        eembed = discord.Embed(title="Help for everyone", value="List of commands for everyone", color=0x1ABC00)
        eembed.set_thumbnail(url="https://ibb.co/db5QKxV")
        eembed.add_field(name="Other commands", value="Commands that can be done by everyone "
                                                      "\n", inline=False)

        eembed.add_field(name="``ùGenerateRace``", value="***Generate a random race*** "
                                                         "\nùGenerateRace", inline=False)

        eembed.add_field(name="``ùTrello``", value="***Send the Trello links of the mod and the bot*** "
                                                   "\nùTrello", inline=True)
        eembed.add_field(name="ùTester", value="***Sends the link of the discord server for testing the bot*** "
                                               "\nùTester", inline=True)

        await ctx.send(embed=sembed)
        await ctx.send(embed=aembed)
        await ctx.send(embed=eembed)
