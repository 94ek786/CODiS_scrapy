import json

with open('data.json','r') as jsonfile:
    stationId = json.load(jsonfile)
jsonfile.close()

for i in stationId:
    print(i)