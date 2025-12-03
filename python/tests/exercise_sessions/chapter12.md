# Exercise 1: The Dungeon Crawler (Maze Runner)

## Task Description

You are trapped in a dark dungeon! Your goal is to write a Python program that navigates a player through a 5x5 grid to find the exit.

You must use the following hardcoded map in your code:

```python
maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "#"],
    [".", ".", ".", ".", "E"]
]
```

- `S` = Start (Player starts here)
- `.` = Open path
- `#` = Wall (Cannot move here)
- `E` = Exit (Win condition)

**Requirements:**

1.  The player starts at the position of 'S' (0, 0).
2.  The program should loop infinitely, asking the user for a move command: `N` (North/Up), `S` (South/Down), `E` (East/Right), `W` (West/Left).
3.  Based on the input, calculate the new coordinates.
4.  **Check for boundaries:** If the move would take the player off the 5x5 grid, print `"You can't go there!"` and do not move.
5.  **Check for walls:** If the new position is a `#`, print `"There is a wall there!"` and do not move.
6.  **Check for Exit:** If the new position is `E`, print `"You found the exit! You win!"` and end the program.
7.  If the move is valid, update the player's position and print the new coordinates (or the map).

## Scoring (5 Points Total)

The automatic grader will run your script and feed it inputs to test different scenarios.

- **[1 Point] Initialization:** Player starts correctly at (0,0).
- **[1 Point] Valid Movement:** Player can move to an open spot (e.g., East from start).
- **[1 Point] Wall Collision:** Player cannot move into a wall (`#`).
- **[1 Point] Boundary Check:** Player cannot move off the map (e.g., North from start).
- **[1 Point] Win Condition:** Reaching `E` prints the win message and exits.

## Example Run

```text
Current position: (0, 0)
Move (N/S/E/W): N
You can't go there!
Current position: (0, 0)
Move (N/S/E/W): E
Current position: (0, 1)
Move (N/S/E/W): S
There is a wall there!
...
```
Name the file as `maze_runner.py` and name the function that contains all your logic as `main()`.

# Exercise 2: The TV Guide (Data Fetching)

## Task Description

In this task, you will create a Command Line Interface (CLI) tool that fetches information about TV shows from the internet. You will use the **TVMaze API**, which is free and requires no authentication.

**API Endpoint:** `https://api.tvmaze.com/search/shows?q=<QUERY>`

- Replace `<QUERY>` with the show name (e.g., `girls`, `breaking bad`).
- The API returns a JSON list of results. You usually want the first result (`[0]`).
- Inside the result, the data is in the `show` dictionary.

**Requirements:**

1.  Ask the user for a search term: `Enter show name: `
2.  Use the `requests` library (or `urllib`) to fetch data from the API.
3.  If no results are found, print `"No shows found."`
4.  If a show is found, print the following details:
    - **Name:** The name of the show.
    - **Premiered:** The date it premiered.
    - **Summary:** The summary of the show (Note: The API returns HTML tags like `<p>` in the summary. You do not need to remove them, but it's a bonus if you do).

## Scoring (5 Points Total)

The automatic grader will run your script and simulate user input.

- **[1 Point] Input:** The program correctly asks for input.
- **[1 Point] Request:** The program successfully makes an HTTP request to the TVMaze API.
- **[1 Point] Name:** The output contains the correct show name (e.g., "Breaking Bad").
- **[1 Point] Premiered:** The output contains the correct premiere date (e.g., "2008-01-20").
- **[1 Point] Summary:** The output contains the show summary text.

## Example Run

```text
Enter show name: Breaking Bad
Name: Breaking Bad
Premiered: 2008-01-20
Summary: <p>Breaking Bad follows protagonist Walter White, a chemistry teacher...</p>
```

Name the file as `tv_guide.py` and name the function that contains all your logic as `main()`.

# Exercise 3: The Server-Side Calculator (Flask)

## Task Description

In this task, you will build a simple web application using **Flask**. The User Interface (HTML/CSS/JS) is already provided for you. Your job is to write the **Python Backend** that performs the calculations.

**The Architecture:**

1.  **Frontend (Provided):** A beautiful "Neon" calculator that runs in the browser. When you press `=`, it sends a request to your server.
2.  **Backend (You write this):** A Flask app that listens for these requests, does the math, and returns the answer.

**Requirements:**

1.  Create a Flask application (`app.py`).
2.  Create a route `/` that renders the provided `index.html` template.
3.  Create a route `/calculate` that accepts three query parameters:
    - `a`: The first number (e.g., `10`).
    - `b`: The second number (e.g., `5`).
    - `op`: The operation (`add`, `sub`, `mul`, `div`).s
4.  The `/calculate` route must return a JSON object with the result: `{"result": 15}`.
5.  Handle division by zero by returning `{"result": "Error"}`.

## Provided Files

You must create a folder named `templates` and place the provided `index.html` file inside it.

## Scoring (5 Points Total)

The automatic grader will run your Flask app in the background and send HTTP requests to it using `curl` or Python's `requests`.

- **[1 Point] Web Server:** The Flask app starts and serves the index page at `/`.
- **[1 Point] Addition:** `/calculate?a=10&b=20&op=add` returns `30`.
- **[1 Point] Subtraction:** `/calculate?a=10&b=3&op=sub` returns `7`.
- **[1 Point] Multiplication:** `/calculate?a=5&b=5&op=mul` returns `25`.
- **[1 Point] Division:** `/calculate?a=10&b=2&op=div` returns `5.0` (or `5`).

## Example Usage

If you run your app and visit `http://127.0.0.1:5000/calculate?a=10&b=2&op=add` in your browser, you should see:

```json
{
  "result": 12
}
```

Name the file as `app.py`. It should have the `@app.route('/')`, and `@app.route('/calculate')` decorators.


# Exercise 4: The Todo List Manager (CLI + Files)

## Task Description

In this task, you will create a command-line tool to manage a Todo list. The list will be saved to a file named `todo.txt` so that your tasks are remembered even after you close the program.

You will use `sys.argv` to read command line arguments.

**Usage:**

1.  **Add a task:** `python todo.py add "Buy Milk"`
    - Appends "Buy Milk" to `todo.txt`.
    - Prints `Task added.`
2.  **List tasks:** `python todo.py list`
    - Reads `todo.txt`.
    - Prints all tasks with their line number (1-based).
    - Example output:
      ```
      1. Buy Milk
      2. Walk the dog
      ```
3.  **Delete a task:** `python todo.py delete 1`
    - Deletes the task at line 1.
    - Rewrites the file without that line.
    - Prints `Task deleted.`

**Requirements:**

- Use `sys.argv` to determine the command (`add`, `list`, `delete`).
- Use `open(filename, 'a')` to append.
- Use `open(filename, 'r')` to read.
- Use `open(filename, 'w')` to rewrite the file (for delete).
- Handle the case where `todo.txt` does not exist yet (e.g., for `list` command).

## Scoring (5 Points Total)

The automatic grader will run your script with different arguments and check the content of `todo.txt` and the output.

- **[1 Point] Add:** `python todo.py add "Task 1"` correctly appends to the file.
- **[1 Point] Persistence:** Adding a second task preserves the first one.
- **[1 Point] List:** `python todo.py list` prints tasks with numbers (e.g., "1. Task 1").
- **[1 Point] Delete:** `python todo.py delete 1` correctly removes the line from the file.
- **[1 Point] Error Handling:** `list` works even if the file doesn't exist (prints nothing or "Empty").

## Example Run

```bash
$ python todo.py add "Learn Python"
Task added.
$ python todo.py add "Sleep"
Task added.
$ python todo.py list
1. Learn Python
2. Sleep
$ python todo.py delete 1
Task deleted.
$ python todo.py list
1. Sleep
```

Name the file as `todo.py` and the main function that handles all the logic as `main()`.