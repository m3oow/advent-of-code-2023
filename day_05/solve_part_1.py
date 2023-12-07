def extract_vectors(index, array):
    temp_index = 0
    for line in array[index + 1:]:
        if "map" in line: break
        temp_index += 1
    return [x for x in array[index + 1:index + 1 + temp_index]]

file = open("./day_05/input.txt", "r")

file_as_array = [x.strip() for x in file.readlines() if x != "\n"]
vectors = []

for index, line in enumerate(file_as_array):
    if "seeds" in line:
        seeds = line.split(":")[1].strip().split(" ")
    if "map" in line:
        vectors.append(extract_vectors(index, file_as_array))

result = []
for seed in seeds:

    current_value = seed
    for vector in vectors:
        trace = current_value
        for entry in vector:
            destination = int(entry.split(" ")[0])
            source = int(entry.split(" ")[1])
            interval = int(entry.split(" ")[2])
            
            if source <= int(current_value) <= source + interval - 1:
                current_value = destination + (int(current_value) - source)
                break
    result.append(current_value)
    print(f"Best location for seed {seed} is {current_value}")
print(f"The result is: {min(result)}")

file.close()
