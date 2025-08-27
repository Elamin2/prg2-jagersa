print("skapa din häst!")


player_horse = {
    "name":"",
    "speed":65,
    "agility":40,
}

def input_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        expect ValueError:
        print("invalid input. Please enter a number.")        

player_horse["name"] = input("vad ska din häst heta: ")
print("Din häst har speed och agility, max 6 i en stat, max 8 totalt. ")
while player_horse["speed"] + player_horse["agility"] < 8:

    player_horse["speed"] = input_int("hur snabbt är din häst (1-6): ")
    player_horse["agility"] = input_int("Hur smidig är din häst (1-6): ")

print(player_horse)  




