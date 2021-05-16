from nba_api.stats.endpoints import commonplayerinfo
import requests
import pandas
import pprint
import time

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

#Check the response
print(bool(player_info.get_json()))
print()
print()
print(player_info.get_json())
print()
print()

#Print the result
Lebron = player_info.get_normalized_dict()

pprint.pprint(Lebron)
print()
print()
input("Press any key to end...")