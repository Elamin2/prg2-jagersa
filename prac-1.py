# Fråga användaren för namn
# namnet måste vara minst 2 tecken långt
# annars måste användaren skriva en ny namn

user_name = {
    "name": "",

    } 

def input_int(prompt):
    while True: 
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid name input. Please enter a valid name.")