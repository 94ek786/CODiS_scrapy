
import json

with open('south_station.json','r') as jsonfile:
    stationId = json.load(jsonfile)
jsonfile.close()
print(len(stationId[0]) + len(stationId[1]) + len(stationId[2]))