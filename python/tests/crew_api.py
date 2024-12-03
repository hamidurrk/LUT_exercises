from urllib.request import urlopen
import json


url = "https://api.spacexdata.com/v5/launches/"
def get_url(url, **kwargs):
    if not kwargs:
        url = url
    else:
        url = url + "?" + "&".join([f"{key}={value}" for key, value in kwargs.items()])
    return url

def fetch_data(url):
    with urlopen(url) as response:
        body = json.load(response)
    return body

def json_to_matrix(data, filter_keys=[]):
    matrix = []
    for character in data:
        row = []
        for key in filter_keys:
            if key == "origin":
                row.append(character[key]["name"])
            else:
                row.append(character[key])
        matrix.append(row)
    return matrix
            
def get_filtered_characters(limit, **kwargs):
    all_data = []
    for page in range(1, limit+1):
        if page == 1:
            url = get_url(**kwargs)
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
# print(json.dumps(data, indent=4))
# print(data[0].keys())
crewed_missions = []
for launch in data:
    if launch["crew"]:
        crewed_missions.append(launch)

print(json.dumps(crewed_missions, indent=4))
