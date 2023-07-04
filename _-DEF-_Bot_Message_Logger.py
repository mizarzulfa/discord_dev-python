import discord
from auth.privateToken import myToken


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(str(message.content))  # string value


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(myToken())
