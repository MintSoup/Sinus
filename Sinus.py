import discord
import aiohttp
import json
import asyncio
import random
import os

class MyClient(discord.Client):



    def __init__(self, **options):
        super().__init__(**options)
        self.serverData = {}

    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name='sinus.glitch.me'))

       
                
    
    async def on_message(self, message):

        #house-keeping stuff-----------------------------------------------------------

        channel = message.channel
        author = message.author
      
        assert isinstance(message, discord.Message)
        assert isinstance(channel, discord.TextChannel)
        assert isinstance(author, discord.Member)

        if message.author == self.user:
            return
        #-----------------------------------------------------------------------------

        if not channel.guild.id in self.serverData:
            await self.updateSettings(channel.guild.id)
            msg = await channel.send("Updating config for this server...")
           
            if channel.guild.id in self.serverData:
                await msg.edit(content="Updated config for this server.")
            else:
                await msg.edit(content="This server does not appear to have configuration. Please configure it at http://sinusconfigurator.herokuapp.com/" + str(channel.guild.id))
            

        




        data = self.serverData[message.guild.id]
        if message.content.startswith(data["prefix"]):
            command = message.content[len(data["prefix"]):]
            assert isinstance(command, str)


            if command == "reload":
                await self.updateSettings(channel.guild.id)
                msg = await channel.send("Updating config for this server...")
           
                if channel.guild.id in self.serverData:
                    await msg.edit(content="Updated config for this server.")
                else:
                    await msg.edit(content="This server does not appear to have configuration. Please configure it at http://sinusconfigurator.herokuapp.com/" + str(channel.guild.id))







            elif command.startswith("mute") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[5:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        emb = self.embed(int(data["embedcolor"], base=16),
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "muted").replace("{MODERATOR}", author.name),
                        data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.add_roles(discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["mutedRole"])))
                       






                       
            elif command.startswith("kick") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[5:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        emb = self.embed(int(data["embedcolor"], base=16),
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "kicked").replace("{MODERATOR}", author.name),
                        data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.kick()






                        
            elif command.startswith("unban") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[6:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        emb = self.embed(int(data["embedcolor"], base=16),
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "unbanned").replace("{MODERATOR}", author.name),
                        data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.remove_roles(discord.utils.get(muted.roles, id=int(data["modcommands"]["bannedRole"])))







            elif command.startswith("unmute") and data["modcommands"]["enabled"]:  
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[7:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        emb = self.embed(int(data["embedcolor"], base=16),
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "unmuted").replace("{MODERATOR}", author.name),
                        data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.remove_roles(discord.utils.get(muted.roles, id=int(data["modcommands"]["mutedRole"])))








            elif command.startswith("ban") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[4:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        emb = self.embed(int(data["embedcolor"], base=16),
                         data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "banned").replace("{MODERATOR}", author.name),
                         data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.add_roles(discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["bannedRole"])))
                        





            elif command.startswith("purge"):
                if not data["purge"]["enabled"]:
                    return

                if not discord.utils.get(channel.guild.roles, id=int(data["purge"]["permissionRole"])) in author.roles:
                    await channel.send(data["rejected"])
                else:
                    try:
                        todlt = min(500,data["purge"]["maxamount"])
                        todlt = min(todlt, int(command[6:])+1)
                        await channel.purge(limit=todlt)
                        await channel.send(data["purge"]["success"].replace("{AMOUNT}",str(todlt-1)), delete_after=3)

                    except ValueError:
                        await channel.send(data["purge"]["invalidNumber"])







            elif command.startswith("tempban") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[8:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        duration = 0
                        await channel.send(data["modcommands"]["messages"]["duration"])
                        durmsg = await self.wait_for('message', check=lambda d: d.author == author)
                        try:
                            duration = int(durmsg.content)
                            if duration < 0 :
                                raise ValueError("Duration < 0")
                        except ValueError:
                            await channel.send(data["modcommands"]["messages"]["invalidduration"])
                            return

                        emb = self.embed(int(data["embedcolor"], base=16),
                         data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "temporarily banned").replace("{MODERATOR}", author.name),
                         data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.add_roles(discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["bannedRole"])))
                        await asyncio.sleep(duration)
                        await muted.remove_roles(discord.utils.get(muted.roles, id=int(data["modcommands"]["bannedRole"])))








            elif command.startswith("tempmute") and data["modcommands"]["enabled"]:
                
                moderatorRole = discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["permissionRole"]))
                if not moderatorRole in author.roles:
                    await channel.send(data["rejected"])
                else:
                    muted = discord.utils.get(channel.guild.members, mention=command[9:])
                    if not muted:
                        await channel.send(data["modcommands"]["messages"]["usernotfound"])
                    else:
                        assert isinstance(muted, discord.Member)
                        await channel.send(data["modcommands"]["messages"]["reason"])
                        reason = await self.wait_for('message', check=lambda d: d.author == author)
                        duration = 0
                        await channel.send(data["modcommands"]["messages"]["duration"])
                        durmsg = await self.wait_for('message', check=lambda d: d.author == author)
                        try:
                            duration = int(durmsg.content)
                            if duration < 0 :
                                raise ValueError("Duration < 0")
                        except ValueError:
                            await channel.send(data["modcommands"]["messages"]["invalidduration"])
                            return

                        emb = self.embed(int(data["embedcolor"], base=16),
                         data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "temporarily muted").replace("{MODERATOR}", author.name),
                         data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.add_roles(discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["mutedRole"])))
                        await asyncio.sleep(duration)
                        await muted.remove_roles(discord.utils.get(muted.roles, id=int(data["modcommands"]["mutedRole"])))

            



            elif command=="ids":
                e = self.embed(int(data["embedcolor"],16),"IDs","")
                roles=""
                for role in channel.guild.roles[1:]:
                    roles += "name: id\n".replace("name",role.name).replace("id",str(role.id))

                channels = ""
                for chnl in channel.guild.text_channels:
                    channels += "name: id\n".replace("name",chnl.mention).replace("id",str(chnl.id))
                

                e.add_field(name="Roles",value=roles)
                e.add_field(name="Channels",value=channels)

                await channel.send(embed=e)














            elif command == "help":
                            e = self.embed(int(data["embedcolor"],16), "Help", "")
                            assert isinstance(e, discord.Embed)
                            if data["modcommands"]["enabled"]:
                                e.add_field(name="Moderator commands", value="""
                                {p}ban/unban <@Member> - ban/unban someone
                                {p}kick <@Member> - kick someone
                                {p}mute/unmute <@Member> - mutes/unmute someone 
                                {p}tempban <@Member> - temporarily ban someone
                                {p}tempmute <@Member> - temporarily mute someone
                                """.replace("{p}", data["prefix"]))
                            if data["purge"]["enabled"]:
                                e.add_field(name="Purge",value="{p}purge <n> - removes the last n messages from this channel".replace("{p}",data["prefix"]))


                            e.add_field(name="Technical",value="""
                            {p}reload - reloads the settings of this server. Use this once you have made changes in your configuration
                            {p}ids - shows the ids of all channels and roles. Use this to configure the bot.
                            """.replace("{p}",data["prefix"]))

                            await channel.send(embed=e)





    def embed(self, color, title, body):
        embed = discord.Embed(title=title, description=body, color=color)
        return embed



    async def on_member_join(self,member):
        if member == self.user:
            return

        if member.guild.id in self.serverData:
            data = self.serverData[member.guild.id]
            if data["welcome"]["enabled"]:
               await discord.utils.get(member.guild.channels,
               id=int(data["welcome"]["channel"])).send(data["welcome"]["message"].replace("{MEMBER}", member.mention))
            if data["autorole"]["enabled"]:
                await member.add_roles(discord.utils.get(member.guild.roles, id=int(data["autorole"]["id"])))


    async def on_guild_join(self,guild):
        settings = {
            
            "prefix": ">>",
            "embedcolor": "00ff00",
            "rejected": "You do not have permission to use that command.",

            "autorole":{
                "enabled": False,
                "id": "0"
            },
            "welcome":{
                "enabled": False,
                "channel": "0",
                "message":"Welcome, {MEMBER}! Enjoy your stay!"
            },

            "purge":{
                "enabled": False,
                "maxamount": 100,
                "permissionRole": "0",
                "invalidNumber": "Please give a valid number.",
                "success": "Deleted {AMOUNT} messages."
            },

            "modcommands": {
                "enabled": False,
                "messages": {
                    "body": "Reason: {REASON}",
                    "title": "{MEMBER} was {ACTION} by {MODERATOR}",
                    "usernotfound": "That member does not exist on this server.",
                    "reason": "Reason:",
                    "duration": "Duration (seconds):",
                    "invalidduration": "Invalid duration."
                },
                "bannedRole": "0",
                "mutedRole": "0", 
                "permissionRole": "0"
            }
        }
        passwd = ""
        passchars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for lol in range(16):
            passwd += passchars[random.randrange(0,len(passchars))]

        async with aiohttp.ClientSession() as session:
            async with session.post('http://sinus.glitch.me/set/'+str(guild.id),data={"password": passwd,"settings": json.dumps(settings)}) as resp:
                txt = await resp.text()
                print(txt)

        await guild.owner.send("Thank you for using Sinus. You can configure the settings for your server over at http://sinus.glitch.me/"+str(guild.id)+" using the password " + passwd)

        

    async def on_guild_remove(self,guild):
        guildids = [str(guild.id) for guild in self.guilds]
        async with aiohttp.ClientSession() as session:
            async with session.get('http://sinus.glitch.me/servers',params={"password": os.environ["pass"], "servers":json.dumps(guildids)}) as resp:
                txt = await resp.text()
                print(txt)

            
            


    async def updateSettings(self,id):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://sinus.glitch.me/settings/'+str(id)) as resp:
                txt = await resp.text()
                if not txt == "invalid id":
                    self.serverData[id] = json.loads(txt)








client = MyClient()
client.run(os.environ["token"])