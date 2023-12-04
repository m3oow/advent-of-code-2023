schematics = []
result = []

def find_adjacencies(line_number, column_number):
    candidates = []
    # Check the line above
    if line_index > 0:
        # Upper left
        if column_index > 0:
            if schematics[line_index - 1][column_index - 1].isdigit(): candidates.append((line_index - 1, column_index - 1))
        # Upper right
        if column_index < 139:
            if schematics[line_index - 1][column_index + 1].isdigit(): candidates.append((line_index - 1, column_index + 1))
        # Upper Middle
        if schematics[line_index - 1][column_index].isdigit(): candidates.append((line_index - 1, column_index))
    
    if line_index < len(schematics) - 1:
        # Bottom left
        if column_index > 0:
            if schematics[line_index + 1][column_index - 1].isdigit(): candidates.append((line_index + 1, column_index - 1))
        # Bottom right
        if column_index < 139:
            if schematics[line_index + 1][column_index + 1].isdigit(): candidates.append((line_index + 1, column_index + 1))
        # Bottom Middle
        if schematics[line_index + 1][column_index].isdigit(): candidates.append((line_index + 1, column_index))

    # Left
    if column_index > 0:
        if schematics[line_index][column_index - 1].isdigit(): candidates.append((line_index, column_index - 1))
    # Right
    if column_index < 139:
        if schematics[line_index][column_index + 1].isdigit(): candidates.append((line_index, column_index + 1))    
    
    if len(candidates) == 1:
        return 0
    return(complete_numbers(candidates))


def complete_numbers(candidates):
    temp = []
    result = []
    for candidate in candidates:
        if candidate not in result:
            result = []
            result.append(candidate)

            # First, go left
            end = False
            line = candidate[0]
            col = candidate[1]
            
            while not end:
                if col > 0:
                    if schematics[line][col - 1].isdigit():
                        result.append((line, col - 1))
                        col -= 1
                    else:
                        end = True
                else: break

            # Then, go right
            end = False
            line = candidate[0]
            col = candidate[1]
            
            while not end:
                if col < 139:
                    if schematics[line][col + 1].isdigit():
                        result.append((line, col + 1))
                        col += 1
                    else:
                        end = True
                else: break

            temp.append(sorted(result))
                
    #print(f"{candidates} => {temp}")
    return(temp)

def power(numbers):
    result = 1
    for elt in numbers:
        number = ""
        for l,c in elt:
            number += schematics[l][c]
        result *= int(number)
    return result

file = open("./day_03/input.txt", "r")

# First, create a 2D array representing
# the engine schematics
for line in file:
    temp = []
    for char in line.strip():
        temp.append(char)
    schematics.append(temp)

# Then, parse the 2D array to detect stars
# and find their adjacencies

final_result = 0

for line_index, line in enumerate(schematics):
    for column_index, char in enumerate(line):
        if char == "*":
            numbers = find_adjacencies(line_index, column_index)
            if numbers != 0:
                if len(numbers) == 1:
                    continue
                else:
                    print(numbers)
                    final_result += power(numbers)

print(f"The result is: {final_result}")

# print(f"The result is: {sum(result)}")

file.close()