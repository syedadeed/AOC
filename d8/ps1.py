def process_input():
    with open("problem_set.txt", "r") as file:
        path = file.readline().strip()
        file.readline()
        network = dict()
        for i in file.readlines():
            primary_node = i.split("=")[0].strip()
            neighbour_nodes = []
            neighbour_nodes.append(i.split("=")[1].strip()[1:4])
            neighbour_nodes.append(i.split("=")[1].strip()[6:9])
            network.update({primary_node: neighbour_nodes})

        return path, network

path, network = process_input()
current_node = "AAA"
steps = i = 0
while True:
    steps += 1
    if i == len(path):
        i = 0

    if path[i] == "L":
        current_node = network.get(current_node)[0]
    else:
        current_node = network.get(current_node)[1]

    if current_node == "ZZZ":
        break
    i += 1

print(steps)
