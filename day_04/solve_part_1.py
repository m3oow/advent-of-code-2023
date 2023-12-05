import math

file = open("./day_04/input.txt", "r")

final_score = 0

for line in file:
    winners = [x.strip() for x in line.split(":")[1].split("|")[0].strip().split(" ") if x != ""]
    numbers = [x.strip() for x in line.split(":")[1].split("|")[1].strip().split(" ") if x != ""]
    
    number_of_matches = 0
    for number in numbers:
        if number in winners: number_of_matches += 1
    
    if number_of_matches > 0:
        final_score += math.pow(2, number_of_matches - 1)

    # print(f"{line.strip()}")
    # print(f"[+]Winners: {winners}")
    # print(f"[+]Numbers: {numbers}")
    # print(f"[+]Number of matches: {number_of_matches}")

print(f"The result is: {int(final_score)}")

file.close()