import requests
import json

print('Retrieving data from API')

response = requests.get('https://httpbin.org/get').json()

response['headers']['deployment_status'] = 'Active'

push = requests.post('https://httpbin.org/post', json=response)

print(push.json())





#with open('api_config.json', 'w'):
    

