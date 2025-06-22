def get_type(card) -> int:
    condition = True if "J" in card else False

    x = [card.count(i) + 2 for i in {j for j in card}]
    y = 1
    for i in x:
        y *= i

    if y == 7:
        return 7

    if y == 18:
        return 7 if condition else 6

    if y == 20:
        return 7 if condition else 5

    if y == 45:
        return 6 if condition else 4

    if y == 48:
        if condition:
            if card.count("J") == 2:
                return 6
            else:
                return 5
        return 3

    if y == 108:
        return 4 if condition else 2

    if y == 243:
        return 2 if condition else 1

def check(str1: str, str2: str) -> bool:
    strength_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    t_str1 = get_type(str1)
    t_str2 = get_type(str2)

    if t_str1 > t_str2:
        return True
    if t_str1 < t_str2:
        return False

    for i in range(5):
        s_str1 = strength_order.index(str1[i])
        s_str2 = strength_order.index(str2[i])
        if s_str1 > s_str2:
            return True
        if s_str1 < s_str2:
            return False

with open("problem_set.txt", "r") as file:
    data = []
    full_data = dict()
    for i in file.readlines():
        data.append(i.strip().split(" ")[0])
        full_data.update({i.strip().split(" ")[0]: int(i.strip().split(" ")[1])})

    for i in range(len(data)):
        for j in range(i, len(data)):
            if check(data[i], data[j]):
                data[i], data[j] = data[j], data[i]
    ans = 0
    for i in range(len(data)):
        ans += (i + 1) * full_data.get(data[i])
    print(ans)
