with open("problem_set.txt", "r") as file:
    data = [i.strip() for i in file.readlines()]

data_copy = data

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def extract_number(i, j):
    if not check_number(i, j):
        return None

    number = data[i][j]

    start_pos = j - 1
    while check_number(i, start_pos):
        number = data[i][start_pos] + number
        start_pos -= 1

    end_pos = j + 1
    while check_number(i, end_pos):
        number += data[i][end_pos]
        end_pos += 1

    for k in range(start_pos + 1, end_pos):
        data[i] = data[i][:k] + "." + data[i][k + 1:]

    return int(number)


def check_number(i, j):
    try:
        if data[i][j] in numbers:
            return True
    except Exception:
        pass
    return False

def check_surrounding(i, j):
    global data
    x = []
    x.append(extract_number(i, j + 1))
    x.append(extract_number(i, j - 1))
    x.append(extract_number(i + 1, j))
    x.append(extract_number(i + 1, j + 1))
    x.append(extract_number(i + 1, j - 1))
    x.append(extract_number(i - 1, j))
    x.append(extract_number(i - 1, j + 1))
    x.append(extract_number(i - 1, j - 1))
    passes = 0
    gear = 1
    data = data_copy
    for i in x:
        if i is not None:
            passes += 1
            gear *= i
    if passes == 2:
        return gear
    else:
        return 0

total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != "." and data[i][j] not in numbers:
            total += check_surrounding(i, j)
print(total)
