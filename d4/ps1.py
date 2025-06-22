with open("problem_set.txt", "r") as file:
    total = 0
    for i in file.readlines():
        collection = i.strip().split(":")[1].split("|")
        wining_number = collection[0].strip().split(" ")
        alloted_number = collection[1].strip()
        total_wins = -1
        for i in alloted_number.split(" "):
            if i == "":
                continue
            if i in wining_number:
                total_wins += 1
        if total_wins == -1:
            continue
        else:
            total += pow(2, total_wins)
print(total)
