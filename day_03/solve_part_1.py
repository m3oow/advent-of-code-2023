schematics = []
result = []

def issymbol(char):
    if 33 <= ord(char) <= 47 and ord(char) != 46:
        return True
    elif 58 <= ord(char) <= 64:
        return True
    return False

def ispartnumber(line_index, column_index, column_len):
    # Check the line above
    if line_index > 0:
        if column_index > 0:
            if issymbol(schematics[line_index - 1][column_index - 1]): return True
        if column_index < column_len - 1:
            if issymbol(schematics[line_index - 1][column_index + 1]): return True
        if issymbol(schematics[line_index - 1][column_index]): return True
    
    # Check the current line
    if column_index > 0:
        if issymbol(schematics[line_index][column_index - 1]): return True
    if column_index < column_len - 1:
        if issymbol(schematics[line_index][column_index + 1]): return True
    
    # Check the line bellow
    if line_index < len(schematics) - 1:
        if column_index > 0:
            if issymbol(schematics[line_index + 1][column_index - 1]): return True
        if column_index < column_len - 1:
            if issymbol(schematics[line_index + 1][column_index + 1]): return True
        if issymbol(schematics[line_index + 1][column_index]): return True
    
    return False

file = open("./day_03/input.txt", "r")

# First, create a 2D array representing
# the engine schematics
for line in file:
    temp = []
    for char in line.strip():
        temp.append(char)
    schematics.append(temp)

# Then, parse the 2D array to detect part numbers
for line_index, line in enumerate(schematics):
    is_part_number = False
    previous_digit = False
    current_digit = ""

    for column_index, char in enumerate(line):
        if char.isdigit():
            previous_digit = True
            current_digit += char
            if ispartnumber(line_index, column_index, len(line)):
                is_part_number = True

        elif previous_digit and is_part_number:
            result.append(int(current_digit))
            is_part_number = False
            previous_digit = False
            current_digit = ""
        
        else:
            is_part_number = False
            previous_digit = False
            current_digit = ""

    if previous_digit and is_part_number:
        result.append(int(current_digit))

print(f"The result is: {sum(result)}")

file.close()