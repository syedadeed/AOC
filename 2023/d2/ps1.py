def check_valid_game(y: str):
    y = y.split(":")
    game_id = int(y[0][5:])

    max_red = 12
    max_green = 13
    max_blue = 14

    for i in y[1].split(";"):
        for j in i.split(","):
            x = j.strip().split(" ")
            if x[1] == "red" and int(x[0]) > max_red:
                return 0
            elif x[1] == "blue" and int(x[0]) > max_blue:
                return 0
            elif x[1] == "green" and int(x[0]) > max_green:
                return 0

    return game_id

with open("problem_set.txt", "r") as file:
    total = 0
    for i in file.readlines():
        total += check_valid_game(i)
    print(total)
