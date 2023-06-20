import discord
from privateToken import myToken


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'hello':
            await message.channel.send('anjay')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(myToken())