import re

file = open("./day_04/input.txt", "r")

win_cards_id = []

for line in file:
    game_id = re.findall(r'(\d+):', line)[0]
    winners = [x.strip() for x in line.split(":")[1].split("|")[0].strip().split(" ") if x != ""]
    numbers = [x.strip() for x in line.split(":")[1].split("|")[1].strip().split(" ") if x != ""]
    
    number_of_matches = 0
    for number in numbers:
        if number in winners: number_of_matches += 1
    
    # Check if the Card has been gained in previous game
    number_of_free_card = win_cards_id.count(game_id)

    if number_of_matches > 0:
        for i in range (int(game_id) + 1, int(game_id) + 1 + number_of_matches):
            win_cards_id.append(str(i))
        if number_of_free_card > 0:
            for j in range(number_of_free_card):
                for i in range (int(game_id) + 1, int(game_id) + 1 + number_of_matches):
                    win_cards_id.append(str(i))
        
    
    # print(f"[+]Game ID: {game_id}")
    # print(f"[+]Winners: {winners}")
    # print(f"[+]Numbers: {numbers}")
    # print(f"[+]Number of matches: {number_of_matches}")
    # print(f"[+]You win: {win_cards_id}")
    # print(f"-----------------------------\n")

print(f"The result is: {len(win_cards_id) + 205}")

file.close()
