def process_input() -> tuple:
    with open("problem_set.txt", "r") as file:
        sanitized_data = []
        seed = [int(i) for i in file.readline()[7:].strip().split(" ")]
        sanitized_data.append(seed)

        source_to_destination_map = []

        for i in file.readlines():
            if i[0].isdigit():
                source_to_destination_map.append([int(k) for k in i.strip().split(" ")])
            else:
                if source_to_destination_map == []:
                    continue
                sanitized_data.append(source_to_destination_map)
                source_to_destination_map = []

        sanitized_data.append(source_to_destination_map)

        return sanitized_data

def find_mapping(map_values, source) -> list:
    maping = {i: i for i in source}
    for i in range(len(source)):
        for j in range(len(map_values)):
            if source[i] >= map_values[j][1] and source[i] < map_values[j][1] + map_values[j][2]:
                x = source[i] - map_values[j][1]
                maping.update({source[i]: map_values[j][0] + x})

    return list(maping.values())

data = process_input()
location = data[0]

for i in data[1:]:
    location = find_mapping(i, location)

print(min(location))
