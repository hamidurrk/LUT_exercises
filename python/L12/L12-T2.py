# L12-T2: Fetching data from the web – Rick & Morty characters
#
# Written by: Md Hamidur Rahman Khan
#

from urllib.request import urlopen
import json

# url = "https://rickandmortyapi.com/api/character"
# with urlopen(url) as response:
#     body = json.load(response)
# print(body)

class RickAndMortyCharacter:
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/character"
        self.colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
    def fetch_data(self, **kwargs):
        if not kwargs:
            url = self.url
        else:
            url = self.url + "?" + "&".join([f"{key}={value}" for key, value in kwargs.items()])
        with urlopen(url) as response:
            body = json.load(response)
        return body
    
    def json_to_matrix(self, data):
        data = data["results"]
        return [[item[key] for key in data[0].keys()] for item in data]

    def print_colored_json(self, data):
        def print_dict(d, indent=0):
            for key, value in d.items():
                print(f"{' ' * indent}{self.colors['red']}{key}{self.colors['reset']}: ", end="")
                if isinstance(value, dict):
                    print()
                    print_dict(value, indent + 4)
                elif isinstance(value, list):
                    print("[")
                    for item in value:
                        if isinstance(item, dict):
                            print_dict(item, indent + 4)
                        else:
                            print(f"{' ' * (indent + 4)}{item}")
                    print(f"{' ' * indent}]")
                else:
                    print(value)

        if isinstance(data, dict):
            print_dict(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    print_dict(item)
                else:
                    print(item)
    
    def main(self):
        data = self.fetch_data(name="Rick")

        self.print_colored_json(data)
        # print(json.dumps(data, indent=2)) 

if __name__ == "__main__":
    RickAndMortyCharacter().main()
    
    