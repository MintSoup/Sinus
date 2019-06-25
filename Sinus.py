import discord
import aiohttp
import json

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

        self.serverData = {}
                
    
    async def on_message(self, message):

        #house-keeping stuff-----------------------------------------------------------

        channel = message.channel
        author = message.author
        
        assert isinstance(message, discord.Message)
        assert isinstance(channel, discord.TextChannel)
        assert isinstance(author, discord.User)

        if message.author == self.user:
            return
        #-----------------------------------------------------------------------------
            




    def embed(self, color, title, body):
        embed = discord.Embed(title=title, description=body, color=color)
        return embed


    async def updateSettings(self,id):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://sinusconfigurator.herokuapp.com/settings/'+id) as resp:
                self.serverData[id] = json.loads(await resp.text())







if __name__ == "__main__":
    client = MyClient()
    client.run('NTkzMTI2NzU0ODMxNTY0ODAw.XRJXAg.HqYyCObz-KpsjqYmQLna34oAuP0')