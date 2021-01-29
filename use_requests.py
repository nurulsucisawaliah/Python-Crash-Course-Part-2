import requests

url = 'https://detik.com'
response = requests.get(url)
if response.status_code == 200:
    print(f'sukses response = {response.status_code}')
    print(f'contentnya adalah {response.text}')
else:
    print(f'wohooo ada kesalahan requests {response.status_code}')
