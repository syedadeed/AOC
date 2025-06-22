def check_valid_game(y: str):
    y = y.split(":")

    max_red = 0
    max_green = 0
    max_blue = 0

    for i in y[1].split(";"):
        for j in i.split(","):
            x = j.strip().split(" ")
            if x[1] == "red" and int(x[0]) > max_red:
                max_red = int(x[0])
            elif x[1] == "blue" and int(x[0]) > max_blue:
                max_blue = int(x[0])
            elif x[1] == "green" and int(x[0]) > max_green:
                max_green = int(x[0])

    return max_red * max_green * max_blue

with open("problem_set.txt", "r") as file:
    total = 0
    for i in file.readlines():
        total += check_valid_game(i)
    print(total)
