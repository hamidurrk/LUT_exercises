def main():
    maze = [
        ["S", ".", ".", "#", "."],
        ["#", "#", ".", "#", "."],
        [".", ".", ".", ".", "."],
        [".", "#", "#", "#", "#"],
        [".", ".", ".", ".", "E"]
    ]

    x = 0
    y = 0

    print(f"Start position: ({x}, {y})")

    while True:
        move = input("Move (N/S/E/W): ").strip().upper()

        new_x = x
        new_y = y

        if move == "N":
            new_y -= 1
        elif move == "S":
            new_y += 1
        elif move == "E":
            new_x += 1
        elif move == "W":
            new_x -= 1
        else:
            print("Invalid move.")
            continue

        
        if not (0 <= new_x <= 4 and 0 <= new_y <= 4):
            print("You can't go there!")
            continue

        
        if maze[new_y][new_x] == "#":
            print("There is a wall there!")
            continue

        
        x, y = new_x, new_y
        print(f"Current position: ({x}, {y})")

        
        if maze[y][x] == "E":
            print("You found the exit! You win!")
            break


if __name__ == "__main__":
    main()