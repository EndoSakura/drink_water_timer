import requests
import json
import datetime

def upload(path):
    headers = {'Authorization': 'kjmrzN1cUfYDjHWAZcb3wh1Vbcby8bxl'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))


if __name__ == "__main__":
    #upload('C:/Users/wps/Pictures/乃木坂/1.jpg')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    hour = date.split(" ")[1]
    print(hour)