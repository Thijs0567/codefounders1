print('start api read application')

import requests

pagina = requests.get('https://catfact.ninja/facts')
print('pagina')

feitjes = pagina.json()
print(feitjes['current_page'])
print(feitjes['data'][0]['fact'])
