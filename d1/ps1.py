def find_location(location):
    start_num, end_num = None, None

    for i in range(len(location)):
        if location[i].isdigit() and start_num is None:
            start_num = location[i]

        if location[len(location) - i - 1].isdigit() and end_num is None:
            end_num = location[len(location) - i - 1]

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
