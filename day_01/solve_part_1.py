result = 0

with open("input.txt") as file:
    for line in file:
        stripped_line = [c for c in line if c.isdigit()]
        #print(f"{line} => {stripped_line} => {stripped_line[0]}{stripped_line[-1]}")
        result += int(f"{stripped_line[0]}{stripped_line[-1]}")
    print(f"The result is: {result}")