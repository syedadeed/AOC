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

    for rq_source_range in source:
        for i in range(len(map_values)):
            av_destination_range = range(map_values[i][0], map_values[i][0] + map_values[i][2])
            av_source_range = range(map_values[i][1], map_values[i][1] + map_values[i][2])

            common_start = max(av_source_range.start, rq_source_range.start)
            common_end = min(av_source_range.stop, rq_source_range.stop)
            if common_start < common_end:
                x1 = common_start - av_source_range.start
                x2 = common_end - av_source_range.stop
                maping.update({rq_source_range: range(av_destination_range.start + x1, av_destination_range.stop + x2)})

    return list(maping.values())

data = process_input()
location = []
for i in range(0, len(data[0]), 2):
    location.append(range(data[0][i], data[0][i] + data[0][i + 1]))

for i in data[1:]:
    location = find_mapping(i, location)
