import requests


#{'key': '2fde68cfd5d1664e88b13a8a6f5c17198f209aa1'}
def client():
    credentials = {
        'username' : ' testuser',
        'password' : 'cagri1234',       
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/dj-rest-auth/login/',
        data = credentials,
    )

    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()