races = []
result = 1

# Create a list of all races
# 1 tuple = 1 race
file = open("./day_06/input.txt", "r")
times = []
distances = []
for line in file:
    if "Time" in line:
        times = [x.strip() for x in line.split(":")[1].split(' ') if x != ""]
    if "Distance" in line:
        distances = [x.strip() for x in line.split(":")[1].split(' ') if x != ""]
races = [("".join(times), "".join(distances))]
print(races)
file.close()

for index, race in enumerate(races):
    count = 0
    for hold_duration in range(1, int(race[0])):
        traveled_distance = ( int(race[0]) - hold_duration ) * hold_duration
        if traveled_distance >= int(race[1]):
            count +=1
    result *= count
    print(f"Races #{index + 1} => {count}")

print(f"The result is: {result}")
