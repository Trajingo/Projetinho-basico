def run(pokemon):
    import requests
    rqt = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')
    return rqt.json()