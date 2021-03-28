import discord
import os

from commands import hello, dice, pokedex

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    channel = message.channel

    if msg.startswith('$hello'):
        response = hello.run()
        await channel.send(response)

    if msg.startswith('$d') and msg[2:].isdigit():
        faces = int(msg[2:])
        response = dice.run(faces)
        congratz = ""
        if response == faces:
            congratz = "\nVocê rodou o número máximo, que sorte, hein!"
        await channel.send(f"Você rodou um **d{faces}** e tirou **{response}** :game_die:.{congratz}")

    if msg.startswith('$commands'):
        commands = os.listdir("./commands")
        response = "Os comandos disponíveis são: "

        for command in commands:
            response += f"${command}, "
        await channel.send(response[:-2])

    if msg.startswith('$pokedex'):
        pokemon = msg.replace('$pokedex ','')
        response = pokedex.run(pokemon)
        await channel.send(response['id'])

    if msg.startswith('$evolution'):
        pass

client.run('ODIyOTQxMjAxNzU3MzcyNDE2.YFZluA.YFnrH_dea3vhKzUJLKvqB22Z4hw')