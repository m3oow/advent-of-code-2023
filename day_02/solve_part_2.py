def parse(line):
    parsed_result = { 'id': 0, 'red': 0, 'green': 0, 'blue': 0 }

    # Extract the game ID
    parsed_result["id"] = int(line.split(":")[0].strip().split(" ")[1])

    # Extract the game results in a flat array
    game_results = [elt.split(',') for elt in line.split(":")[1].strip().split(";")]
    final_results = []

    for sub_array in game_results:
        for cube in sub_array:
            final_results.append(cube.strip())
    
    # Get the max value per cube color
    for elt in final_results:
        temp = elt.split(" ")
        if parsed_result[temp[1]] < int(temp[0]):
            parsed_result[temp[1]] = int(temp[0])

    return parsed_result


with open("input.txt") as file:
    id_sum = 0

    for line in file:
        result = parse(line)

        cube_power = 1
        if (result["red"] != 1000):
            cube_power *= result["red"]
        if (result["green"] != 1000):
            cube_power *= result["green"]
        if (result["blue"] != 1000):
            cube_power *= result["blue"]

        id_sum += cube_power
        print(f"{line} =s> {result} => {cube_power} => {id_sum}")
    
    print(f"The result is: {id_sum}")
