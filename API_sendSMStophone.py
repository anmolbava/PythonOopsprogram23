import requests
import json

def send_message(number,message):
    url= 'https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization':'sDwAtSZjvxoHdNhY6LGEbrpP9k5n0Bz34c1T2KJgIqliaXCuVfhJLn4fSoBqkHQ6P0KD9piyuFljTbwX',
        'senderid': 'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number
    }
    response = requests.get(url, params=params)
 
    dic = response.json()
    print(dic)

send_message("9209015413","This is youtube message my first python api program")

# the function send message has input for number and message is created to define api endpoint to hit, api key, senderid, number etc.
# response object/variable collects the output from the requests package from get method inside the requests package