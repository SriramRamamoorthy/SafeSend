import discord

token = 'NjI1MDMzOTA2MTE4NDU5NDA5.XYZw6Q.9YpxbEmItE0ivzbOok8z3ngOK4Y'

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
