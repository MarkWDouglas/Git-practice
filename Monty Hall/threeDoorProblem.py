import random

def door_allocation(count_doors, possible_doors, random):
    if random == True:
        door_allocated = random.randint(1, count_doors)
    elif random == False:
        if possible_doors:
            chosen_door = random.choice(list(possible_doors))
        else:
            chosen_door = None
    return door_allocated

def monty_hall_random(num_doors, num_simulations):
    wins = 0
    
    for _ in range(num_simulations):
        # Place the prize behind a random door
        prize_door = door_allocation(num_doors, num_doors, random = True)
        
        # Contestant's initial choice
        initial_choice = door_allocation(num_doors, num_doors, random = True)
        
        # Host opens a door that is neither the prize door nor the initial choice
        available_doors = set(range(1, num_doors + 1)) - {prize_door, initial_choice}
        if available_doors:
            opened_door = random.choice(list(available_doors))
        else:
            # If there are no available doors to open (e.g., in a 2-door scenario),
            # the host doesn't open any door
            opened_door = None
        
        # Contestant switches to a door that is neither their initial choice nor the opened door
        available_switches = set(range(1, num_doors + 1)) - {initial_choice, opened_door}
        if available_switches:
            final_choice = random.choice(list(available_switches))
        else:
            # If there are no available doors to switch to, stick with the initial choice
            final_choice = initial_choice
        
        # Check if the contestant wins
        if final_choice == prize_door:
            wins += 1

    return wins, num_simulations

def monty_hall_play(num_doors):
    
    initial_choice = input('Enter your guess!')

# Example usage
wins, total = monty_hall_random(num_doors=3, num_simulations=10000)
print(f"Wins: {wins}")
print(f"Total simulations: {total}")
print(f"Win rate: {wins/total:.2%}")

def menu():
    print('Welcome to the monty hall simulator!')
    print('Would you like to play the game yourself? or simulate games played?')
    selection = input('Enter your selection (Play/Simulate)').lower()
    if selection == 'play':
        #monty_hall_play():
    elif selection == 'simulate':
        monty_hall_random()
