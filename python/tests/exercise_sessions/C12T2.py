import requests

def main():
    query = input("Enter show name: ").strip()

    url = "https://api.tvmaze.com/search/shows?q=" + query
    response = requests.get(url)

    if response.status_code != 200:
        print("No shows found.")
        return

    data = response.json()

    if not data:
        print("No shows found.")
        return

    show = data[0].get("show", {})

    name = show.get("name") or ""
    premiered = show.get("premiered") or ""
    summary = show.get("summary") or ""

    
    if not (name or premiered or summary):
        print("No shows found.")
        return

    print("Name: " + name)
    print("Premiered: " + premiered)
    print("Summary: " + summary)


if __name__ == "__main__":
    main()