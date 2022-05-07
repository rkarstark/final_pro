from email import header
from lib2to3.pgen2 import token
import requests
import pprint


#{'key': '2fde68cfd5d1664e88b13a8a6f5c17198f209aa1'}
def client():
    
    token = 'Token 2fde68cfd5d1664e88b13a8a6f5c17198f209aa1'

    headers = {
        'Authorization' : token,
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers=headers,
    )

    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()