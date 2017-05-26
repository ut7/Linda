import json

def createJSON(data):
    return { "offreTotal": data[0], "offreDev": data[1], "offreDevJunior": data[2] }

def writeToJsonFile(fileName, data):
    with open(fileName, 'w+') as f:
        json.dump(data, f)
