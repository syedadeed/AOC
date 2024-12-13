# This Solution is not optimal(too slow)
# and the optimal solution assumes a lot of things that are not mentioned in the problem
# Soo all in all i was not able to solve this problem :(
exit()

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
current_nodes = [i for i in network.keys() if i[-1] == "A"]
steps = i = 0

while True:
    steps += 1
    if i == len(path):
        i = 0

    if path[i] == "L":
        for j in range(len(current_nodes)):
            current_nodes[j] = network.get(current_nodes[j])[0]
    else:
        for j in range(len(current_nodes)):
            current_nodes[j] = network.get(current_nodes[j])[1]

    for current_node in current_nodes:
        if current_node[-1] != "Z":
            break
    else:
        break
    i += 1

print(steps)
