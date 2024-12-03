# L12-T2: Fetching data from the web – Rick & Morty characters
#
# Written by: Md Hamidur Rahman Khan
#

from urllib.request import urlopen
import json

class RickAndMortyCharacter:
    def __init__(self):
        self.APP_WIDTH = 100
        self.url = "https://rickandmortyapi.com/api/character"
        self.filter_keys = ["id", "name", "type", "species", "origin", "status"]
        self.menu_options = {
            "0": "Exit",
            "1": "Get all dead characters",
            "2": "Get characters by their name and living status",
        }
        self.colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        self.theme = {
            "title": "magenta",
            "info": "blue",
            "success": "green",
            "warning": "yellow",
            "error": "red"
        }
        
        print(self.print_title("Welcome to Rick & Morty API"))

# ------------------------------ Interface ------------------------------    

    def print_colored(self, text, color, end="", will_return=True):
        colors = self.colors
        if will_return:
            return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
        else:
            print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}", end=end)
    
    def print_title(self, text):
        return self.print_colored(text, self.theme["title"])
        
    def print_info(self, text):
        return self.print_colored(text, self.theme["info"])
    
    def print_success(self, text):
        return self.print_colored(text, self.theme["success"])
    
    def print_warning(self, text):
        return self.print_colored(text, self.theme["warning"])
    
    def print_error(self, text):
        return self.print_colored(text, self.theme["error"])
    
    def print_bar(self, char="-"):
        value = self.APP_WIDTH
        print(f"{char*value}")
    
    def print_colored_json(self, data):
        def print_dict(d, indent=0):
            if indent == 0:
                print("\n"*2)
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
                    
    def print_table_cell_line(self, separator, char, col_widths):
        i = 0
        line = ""
        for width in col_widths:
            if i > 0:
                line += separator
            line += (char * width)
            i += 1
        print(line)
    
    def custom_join(self, separator, list):
        i = 0
        line = ""
        for item in list:
            if i > 0:
                line += separator
            line += str(item)
            i += 1
        return line
    
    def print_table(self, data, title=None,headers=None):
        if headers:
            data.insert(0, headers)
        max_cols = max(len(row) for row in data)
        col_widths = [0] * max_cols
        for row in data:
            i = 0
            for item in row:
                col_widths[i] = max(col_widths[i], len(str(item)))
                i += 1
        if title:
            title = self.print_info(title)
            self.print_table_cell_line("---", "-", col_widths)
            print(f"{title.center(sum(col_widths)+((len(col_widths))*2)+1)}")
            self.print_table_cell_line("---", "-", col_widths)
            
        if headers:
            data.remove(data[0])
            self.print_table_cell_line("=+=", "=", col_widths)
            print(self.custom_join(" | ", (f"{str(item).center(width)}" for item, width in zip(headers, col_widths))))
            self.print_table_cell_line("=+=", "=", col_widths)
        else:
            self.print_table_cell_line("-+-", "-", col_widths)
        
        for row in data:
            padded_row = row + [""] * (max_cols - len(row))
            print(self.custom_join(" | ", (f"{str(item).ljust(width)}" for item, width in zip(padded_row, col_widths))))
            self.print_table_cell_line("-+-", "-", col_widths)
            
# ------------------------------ API Functions ------------------------------

    def get_url(self, **kwargs):
        if not kwargs:
            url = self.url
        else:
            url = self.url + "?" + "&".join([f"{key}={value}" for key, value in kwargs.items()])
        return url
    
    def fetch_data(self, url):
        with urlopen(url) as response:
            body = json.load(response)
        return body
    
    def json_to_matrix(self, data, filter_keys=[]):
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

    def get_input_by_type(self, message, type_):
        while True:
            try:
                value = type_(input(message))
                return value
            except ValueError:
                print(self.print_error("Invalid input! Please try again."))
                
    def get_filtered_characters(self, limit, **kwargs):
        all_data = []
        try:
            for page in range(1, limit+1):
                print(self.print_success(f"Getting page {page} url: "), end="")
                if page == 1:
                    url = self.get_url(**kwargs)
                    data = self.fetch_data(url)
                    total_results = data["info"]["count"]
                    total_pages = data["info"]["pages"]
                else:
                    url = data["info"]["next"]
                    data = self.fetch_data(url)
                print(url)
                all_data += data["results"]
                if page == total_pages:
                    print(self.print_warning("All available pages have been fetched."))
                    break
            return all_data, total_results
        except Exception:
            print(self.print_error(f"An error occurred. Try another entry for API."))
            return [], 0
    
# ------------------------------ Menu Option 1 ------------------------------    
    def get_all_dead_characters(self):
        filter_keys = self.filter_keys
        limit = self.get_input_by_type("Enter limit of pages: ", int)
        all_data, total_results = self.get_filtered_characters(limit, status="dead")
        if all_data != []:
            self.print_table(self.json_to_matrix(all_data, filter_keys), title="All Dead Characters - Rick & Morty", headers=[header.capitalize() for header in filter_keys])
            print(f"{self.print_success("Total number of dead characters:")} {len(all_data)} {self.print_success('out of')} {total_results}")

# ------------------------------ Menu Option 2 ------------------------------    

    def get_characters_by_name_and_status(self):
        filter_keys = self.filter_keys
        name = self.get_input_by_type("Enter character to search for: ", str)
        status = self.get_input_by_type("Enter living status (alive, dead, unknown): ", str)
        limit = self.get_input_by_type("Enter limit of pages: ", int)
        all_data, total_results = self.get_filtered_characters(limit, name=name,status=status)
        if all_data != []:
            self.print_table(self.json_to_matrix(all_data, filter_keys), title="All Dead Characters - Rick & Morty", headers=[header.capitalize() for header in filter_keys])
            print(f"{self.print_success(f"Number of {status} {name}'s found:")} {len(all_data)} {self.print_success('out of')} {total_results}")

# ------------------------------ Menu Functions ------------------------------    

    def menu(self):
        print("You have the following options:")
        for key, value in self.menu_options.items():
            print(self.print_info(f"{key}) {value}"))
        selection = input("Please enter your selection: ")
        if selection not in self.menu_options.keys():
            print(self.print_error("Invalid selection! Please try again.\n"))
            self.menu()
        return selection        
    
    def main(self):
        while True:
            selection = self.menu()
            if selection == "0":
                print(self.print_success("Thank you for using Rick & Morty API."))
                break
            elif selection == "1":
                self.get_all_dead_characters()
            elif selection == "2":
                self.get_characters_by_name_and_status()

if __name__ == "__main__":
    api =RickAndMortyCharacter()
    api.main()
    