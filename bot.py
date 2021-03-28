import discord
import os
import requests


from commands import hello, dice, pokedex
from dotenv import load_dotenv

load_dotenv() 

maleOnly = [
    "braviary", "gallade", "grimmsnarl", "hitmonchan", "hitmonlee",
    "hitmontop", "impidimp", "landorus", "latios", "morgrem",
    "mothim", "nidoking", "nidoran-m", "nidorino", "rufflet",
    "sawk", "tauros", "throh", "thundurus", "tornadus", "tyrogue", "volbeat"
]
femaleOnly = [
    "alcremie", "blissey", "bounsweet", "chansey", "cresselia",
    "flabebe", "floette", "florges", "froslass", "happiny",
    "hatenna", "hatterene", "hattrem", "illumise", "jynx",
    "kangaskhan", "latias", "lilligant", "mandibuzz", "milcery",
    "miltank", "nidoqueen", "nidoran-f", "nidorina", "petilil",
    "salazzle", "smoochum", "steenee", "tsareena", "vespiquen",
    "vullaby", "wormadam"
]

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
        pokemon = msg.replace('$pokedex ','').lower().strip()

        if pokemon == "nidoran":
            data = {
                "id": "10",
                "type": "",
                "tts": "",
                "content": "",
                "pinned": "",
                "mention_everyone": "",
                "activity": "",
                "application": "",
                "webhook_id": "",
                "embeds": "",
                "attachments": "",
                "reactions": "",
                "edited_timestamp": "",
                "flags": "",
                "nonce": ""
            }
            nidorans = ["nidoran-f", "nidoran-m"]
            for nidoran in nidorans:
                fakeMessage = discord.Message(state={}, channel=channel, data=data)
                fakeMessage.content = f"$pokedex {nidoran}"
                fakeMessage.author = ""
                await on_message(fakeMessage)
            return

        data = pokedex.run(pokemon)
        response = f'Não foi possível encontrar o pokémon **{pokemon}**'

        if data['status_code'] != requests.codes.not_found:
            response = '***`'
            response += f'Name: {data["species"]["name"].upper()}\n'
            response += f'ID: {data["id"]}\n'
            response += 'Type:'
            for item in data["types"]: 
                response += f' {item["type"]["name"].upper()} / '
            response = response[:-3]
            response += f'\nWeight: {data["weight"]}\n'
            response += f'Height: {data["height"]}'
            response += '`***'
        await channel.send(response)
        await channel.send(data["sprites"]["front_default"])
        #await channel.send(data["sprites"]["front_female"])

    if msg.startswith('$evolution'):
        pass

client.run(os.getenv("DISCORD_TOKEN"))