generated_card_counts = []

with open("problem_set.txt", "r") as file:
    data = [line.strip().split(":")[1].split("|") for line in file.readlines()]

    for card in data:
        winning_numbers = set(card[0].strip().split(" "))
        winning_numbers.discard("")
        user_numbers = set(card[1].strip().split(" "))
        user_numbers.discard("")

        generated_card_counts.append(len(user_numbers.intersection(winning_numbers)))

card_instances = [1] * len(generated_card_counts)

for i in range(len(card_instances)):
    for j in range(i + 1, i + 1 + generated_card_counts[i]):
        card_instances[j] += card_instances[i]

print(sum(card_instances))
# Yes i wrote this and sorry i know you prolly cant understand it
# yeah i tried the recursive approach, its slow
