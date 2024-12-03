def find_num(substring: str, condition):
    number_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    available_numbers = dict()

    for i in number_names:
        if i in substring:
            if condition == "from start":
                available_numbers.update({substring.index(i): str(number_names.index(i) + 1)})
            elif condition == "from end":
                available_numbers.update({substring.rfind(i): str(number_names.index(i) + 1)})

    if len(available_numbers) == 0:
        return None

    if condition == "from start":
        return available_numbers[min(available_numbers.keys())]
    elif condition == "from end":
        return available_numbers[max(available_numbers.keys())]

def find_location(location):
    start_num, end_num = None, None

    for i in range(len(location)):
        if location[i].isdigit() and start_num is None:
            tmp = find_num(location[:i], "from start")
            if tmp is None:
                start_num = location[i]
            else:
                start_num = tmp

        if location[len(location) - i - 1].isdigit() and end_num is None:
            tmp = find_num(location[len(location) - i:], "from end")
            if tmp is None:
                end_num = location[len(location) - i - 1]
            else:
                end_num = tmp

        if start_num is not None and end_num is not None:
            break

    return int(start_num + end_num)

def main():
    with open("problem_set.txt", "r") as file:
        total = 0
        for location in file.readlines():
            total += find_location(location)
    print(total)

if __name__ == main():
    main()
