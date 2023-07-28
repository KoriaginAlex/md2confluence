import requests
import json
import sys

username = 'admin'
password = '0305'

parentId = 98380
title = sys.argv[1]
print (title)

r = requests.get('http://localhost:8090/rest/api/content/search/?cql=title="'+title+'"&space=SPC&type=page&expand=version',
                 auth = (username, password), verify=True)
if (r.ok):
    # print(r.text)
    data = json.loads(r.text)
    count = len(data['results'])
    
    if (count > 0):
        #need to update post
        id = data['results'][0]['id']
        number = data['results'][0]['version']['number']
        print (id, " :: ", number)
    else:
        #need to create new post
        print ('creating new post')
        URL = 'http://localhost:8090/rest/api/content'
        with open('readme.html', 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        text = text
        PARAMS = {
            "type": "page",
            "ancestors":[{"id":parentId}],
            "title": title,
            "version": {
                "number": 1
                },
            "space": {
                "key": "SPC"
            },
            "body": {
                "storage": {
                    "value": text,
                    "representation": "storage"
                }
            }                
        }
        HEADERS = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        r = requests.post(URL, json=PARAMS, headers=HEADERS, auth = (username, password), verify=True)
        print(r.status_code)
else:
    print(r)