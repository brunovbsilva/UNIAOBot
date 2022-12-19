import json

def readJson(name):
    with open (f'JSONS/{name}.json') as _json:
        return json.load(_json)

def writeJson(name, data):
    with open (f'JSONS/{name}.json','w') as j:
            json.dump(data,j,indent=4)

def isVIP(id):
    with open (f'JSONS/VIP.json') as _json:
        data = json.load(_json)
        if id in data['values']:
            return True
        return False