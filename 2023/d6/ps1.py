import math

def parse_input():
    with open("problem_set.txt", "r") as file:
        line1 = [i for i in file.readline().strip()[5:].strip().split(" ") if i != ""]
        line2 = [i for i in file.readline().strip()[9:].strip().split(" ") if i != ""]
        return {int(line1[i]): int(line2[i]) for i in range(len(line1))}

data = parse_input()
ans = 1
for T, D in data.items():
    x1 = math.floor((T + math.sqrt((T * T) - (4 * D))) / 2)
    x2 = math.ceil((T - math.sqrt((T * T) - (4 * D))) / 2)
    ans *= x1 - x2 + 1

print(ans)
