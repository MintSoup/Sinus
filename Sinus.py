import discord
import aiohttp
import json

class MyClient(discord.Client):



    def __init__(self, **options):
        super().__init__(**options)
        self.serverData = {}

    async def on_ready(self):
        print('Logged on as', self.user)

       
                
    
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
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "muted").replace("{BANNER}", author.name),
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
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "kicked").replace("{BANNER}", author.name),
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
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "unbanned").replace("{BANNER}", author.name),
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
                        data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "unmuted").replace("{BANNER}", author.name),
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
                         data["modcommands"]["messages"]["title"].replace("{MEMBER}", muted.name).replace("{ACTION}", "banned").replace("{BANNER}", author.name),
                         data["modcommands"]["messages"]["body"].replace("{REASON}", reason.content))
                        await channel.send(embed=emb)
                        await muted.send(embed=emb)
                        await muted.add_roles(discord.utils.get(channel.guild.roles, id=int(data["modcommands"]["bannedRole"])))
                        




            elif command.startswith("purge"):
                if not discord.utils.get(channel.guild.roles, id=int(data["purge"]["permissionRole"])) in author.roles:
                    await channel.send(data["rerjected"])
                else:
                    try:
                        todlt = min(500,data["purge"]["maxamount"])
                        todlt = min(todlt, int(command[6:])+1)
                        await channel.purge(limit=todlt)
                        await channel.send(data["purge"]["success"].replace("{AMOUNT}",str(todlt)), delete_after=3)

                    except ValueError:
                        await channel.send(data["purge"]["invalidNumber"])



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

            
            


    async def updateSettings(self,id):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://sinusconfigurator.herokuapp.com/settings/'+str(id)) as resp:
                txt = await resp.text()
                if not txt == "invalid id":
                    self.serverData[id] = json.loads(txt)








if __name__ == "__main__":
    with open("token.txt") as f:
        client = MyClient()
        client.run(f.read())