from urllib.request import urlopen
import json

def get_dead_characters():
    while True:
        limit = input("Enter limit of pages: ")
        try:
            limit = int(limit)
            break
        except:
            print("Invalid input! Please try again.")
    
    url = " https://rickandmortyapi.com/api/character?status=dead"
    data = []
    
    for page in range(1, limit+1):
        with urlopen(url) as response:
            print(f"Getting page {page} url: {url}")
            body = json.load(response)
            data += body["results"]
            url = body["info"]["next"]
            if not url:
                break
    cols = ["id", "name", "type", "species", "origin", "status"]
    for row in data:
        for col in cols:
            if col == "origin":
                print(col + ":", row[col]["name"], end=" - ")
            elif col == "status":
                print(col + ":", row[col], end="\n")
            else:
                print(col + ":", row[col], end=" - ")
    print(f"Total number of {len(data)} dead characters")
            
def get_characters_by_name_and_status():
    name = input("Enter character to search for: ")
    status = input("Enter living status (alive, dead, unknown): ")
    while True:
        limit = input("Enter limit of pages: ")
        try:
            limit = int(limit)
            break
        except:
            print("Invalid input! Please try again.")
    
    url = f" https://rickandmortyapi.com/api/character?name={name}&status={status}"
    data = []
    try:
        for page in range(1, limit+1):
            with urlopen(url) as response:
                print(f"Getting page {page} url: {url}")
                body = json.load(response)
                data += body["results"]
                url = body["info"]["next"]
                if not url:
                    break
    except:
        print("An error occurred. Try another entry for API.")
        return
    
    cols = ["id", "name", "type", "species", "origin", "status"]
    for row in data:
        for col in cols:
            if col == "origin":
                print(col + ":", row[col]["name"], end=" - ")
            elif col == "status":
                print(col + ":", row[col], end="\n")
            else:
                print(col + ":", row[col], end=" - ")
    print(f"Total number of {len(data)} {status} {name}'s found")
    
def menu():
    print("You have the following options")
    print("0) Exit")
    print("1) Get all dead characters")
    print("2) Get characters by their name and living status")
    user_input = input("Enter your choice: ")
    return user_input

def main():
    print("Welcome to Rick & Morty API")
    while True:
        user_input = menu()
        if user_input == "0":
            break
        elif user_input == "1":
            get_dead_characters()
        elif user_input == "2":
            get_characters_by_name_and_status()
        else:
            print("Invalid choice. Please try again.")
            
main()
            