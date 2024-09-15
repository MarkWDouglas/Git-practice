import random

def monty_hall_simulation():
    # Randomly assign the car to one of the three doors
    doors = ['lose', 'lose', 'win']
    random.shuffle(doors)
    
    # Ask user to choose a door (1, 2, or 3)
    user_choice = random.choice(range(3))
    #user_choice = int(input("Choose a door (1, 2, or 3): ")) - 1
    
    # Monty opens a door that reveals a goat (but not the user's chosen door)
    available_doors = [i for i in range(3) if i != user_choice and doors[i] == 'lose']
    monty_opens = random.choice(available_doors)
    
    # Show which door Monty opened
    # print(f"Monty opens door {monty_opens + 1}, revealing a goat.")
    
    # Ask user if they want to stay or swap
    # swap_choice = input("Do you want to stay with your choice or swap? (stay/swap): ").lower()
    swap_choice = random.choice(['stay',])
    # If user chooses to swap, change their choice to the remaining door
    if swap_choice == 'swap':
        user_choice = [i for i in range(3) if i != user_choice and i != monty_opens][0]
    
    # Determine if the user won or lost
    if doors[user_choice] == 'car':
        # print("Congratulations! You won the car!")
        return 1
    else:
        # print("Sorry, you got a goat.")
        return 0
sims = int(input('How many times do you want your simulation to run? '))
win_tally = 0
for i in range(1, sims + 1):
    win_tally = win_tally + monty_hall_simulation()
print(win_tally)
