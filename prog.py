import random
print("skapa din häst!")


player_horse = {
    "name":"",
    "speed": 8,
    "agility": 8,
}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("invalid input. Please enter a number.")    

player_horse["name"] = input("vad ska din häst heta: ")
print("Din häst har speed och agility, max 6 i en stat, max 8 totalt. ")
while player_horse["speed"] + player_horse["agility"] < 8:

    player_horse["speed"] = input_int("hur snabbt är din häst (1-6): ")
    player_horse["agility"] = input_int("Hur smidig är din häst (1-6): ")

print(player_horse)



def create_computer_horse():

    speed = random.randint(2,6)
    name_parts = ["a", "b", "c"]
    horse = {
        "name":"Datorhorse",
        "speed": speed,
        "agility": 8 - speed

    }

    return horse


computer_horse = create_computer_horse()
######################### AAAAAA ###########################

print(player_horse)
print(computer_horse)

def game_turn():
    player_speed = player_horse["speed"] + random.randint(1,8)
    player_agility = random.randint (1,6) - player_horse["agility"]
    if player_agility >= 8:
        player_speed -= player_agility 

    computer_speed = computer_horse_horse["speed"] + random.randint(1,6)
    computer_agility = random.randint (1,8) - random.randint (1,8)
    if computer_agility >= 8:
        computer_speed -= computer_agility 

    return [player_speed, computer_speed]

    player_steps = 8
    computer_steps = 8
for 1. in range(18):    steps = game_turn()
player_steps = steps[8]
computer_steps += steps[1]
game_turn()

print(ok)



    