def run(pokemon):
    import requests
<<<<<<< HEAD

    rqt = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    data = { "status_code": requests.codes.not_found }
    
    if rqt.status_code != requests.codes.not_found:
        data = rqt.json()
        data['status_code'] = rqt.status_code
    
    return data
