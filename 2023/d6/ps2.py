import math
def parse_input():
    with open("problem_set.txt", "r") as file:
        line1 = [i for i in file.readline().strip()[5:].strip().split(" ") if i != ""]
        line2 = [i for i in file.readline().strip()[9:].strip().split(" ") if i != ""]
        T = ""
        for i in line1:
            T += i
        D = ""
        for i in line2:
            D += i
        return (int(T), int(D))

data = parse_input()
T = data[0]
D = data[1]
x1 = math.floor((T + math.sqrt((T * T) - (4 * D))) / 2)
x2 = math.ceil((T - math.sqrt((T * T) - (4 * D))) / 2)
ans = x1 - x2 + 1
