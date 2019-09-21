import discord

token = 'NjI1MDMzOTA2MTE4NDU5NDA5.XYaDEw.hv8iyZyBtUQYfSfKpv6-ylXRiOc'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('fuck you'):
        await message.channel.send('Hey, that isn\'t nice!')

    elif message.content.startswith('bitch'):
        await message.channel.send('Hey, that isn\'t nice!')


client.run(token)
