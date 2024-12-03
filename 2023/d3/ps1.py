with open("problem_set.txt", "r") as file:
    data = [i.strip() for i in file.readlines()]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
part_numbers = []

def extract_number(i, j):
    if not check_number(i, j):
        return

    number = data[i][j]

    start_pos = j - 1
    while check_number(i, start_pos):
        number = data[i][start_pos] + number
        start_pos -= 1

    end_pos = j + 1
    while check_number(i, end_pos):
        number += data[i][end_pos]
        end_pos += 1

    part_numbers.append(int(number))

    for k in range(start_pos + 1, end_pos):
        data[i] = data[i][:k] + "." + data[i][k + 1:]


def check_number(i, j):
    try:
        if data[i][j] in numbers:
            return True
    except Exception:
        pass
    return False

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != "." and data[i][j] not in numbers:
            extract_number(i, j + 1)
            extract_number(i, j - 1)
            extract_number(i + 1, j)
            extract_number(i + 1, j + 1)
            extract_number(i + 1, j - 1)
            extract_number(i - 1, j)
            extract_number(i - 1, j + 1)
            extract_number(i - 1, j - 1)

print(sum(part_numbers))
