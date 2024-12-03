from urllib.request import urlopen
import json
import requests


url = "https://api.spacexdata.com/v5/launches/5eb87d46ffd86e000604b388"

def fetch_data(url):
    with urlopen(url) as response:
        body = json.load(response)
    return body

def fetch_data_requests(url):
    response = requests.get(url).json()
    return response
            
def get_filtered_characters(limit, **kwargs):
    all_data = []
    for page in range(1, limit+1):
        if page == 1:
            data = fetch_data(url)
            total_results = data["info"]["count"]
            total_pages = data["info"]["pages"]
        else:
            url = data["info"]["next"]
            data = fetch_data(url)
        print(url)
        all_data += data["results"]
    return all_data, total_results

data = fetch_data(url)
print(json.dumps(data, indent=4))
# print(data[0].keys())
# crewed_missions = []
# for launch in data:
#     if launch["crew"]:
#         crewed_missions.append(launch)

# print(json.dumps(crewed_missions, indent=4))
