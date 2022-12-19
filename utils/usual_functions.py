import json

def readJson(name):
    with open (f'JSONS/{name}.json') as _json:
        return json.load(_json)

def writeJson(name, data):
    with open (f'JSONS/{name}.json','w') as j:
            json.dump(data,j,indent=4)

def isVIP(id):
    data = readJson('VIP')
    if id in data['values']:
        return True
    return False