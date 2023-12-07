from multiprocessing import Process

INPUT_FILE = "./day_05/input.txt"

def extract_vectors(index, array):
    temp_index = 0
    for line in array[index + 1:]:
        if "map" in line: break
        temp_index += 1
    return [x for x in array[index + 1:index + 1 + temp_index]]

def get_shortest_distance(seeds, vectors):
    # For each seed, folow the transformation and keep
    # only the shortest distance
    result = 0
    print(f"Current seed is: {int(seeds[0])}")
    for j in range(int(seeds[1])):
        seed = int(seeds[0]) + j
        current_value = seed
        for vector in vectors:
            for entry in vector:
                destination = int(entry.split(" ")[0])
                source = int(entry.split(" ")[1])
                interval = int(entry.split(" ")[2])
                
                if source <= int(current_value) <= source + interval - 1:
                    current_value = destination + (int(current_value) - source)
                    break
        if result == 0 or current_value < result:
            result = current_value
    print(f"Best location for seed {seeds[0]} is {result}")

if __name__ == "__main__":
    # Extract input file content in an array
    file = open(INPUT_FILE, "r")
    file_as_array = [x.strip() for x in file.readlines() if x != "\n"]
    file.close()
    
    # Extract a list of seeds and range
    # and the list of transformation vectors
    vectors = []

    for index, line in enumerate(file_as_array):
        if "seeds" in line:
            seeds = line.split(":")[1].strip().split(" ")
        if "map" in line:
            vectors.append(extract_vectors(index, file_as_array))

    # For each seed, folow the transformation and keep
    # only the shortest distance
    procs = []
    for i in range(0, len(seeds), 2):
        proc = Process(target=get_shortest_distance, args=([seeds[i], seeds[i+1]], vectors))
        procs.append(proc)
        proc.start()
    
    # print(f"The result is: {result}")
