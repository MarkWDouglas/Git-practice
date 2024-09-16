import random

def random_allocator(count_doors, possible_doors, isRandom):
    if isRandom == True:
        chosen_door = random.randint(1, count_doors)
    elif isRandom == False:
        if possible_doors:
            chosen_door = random.choice(list(possible_doors))
        else:
            print('There are no available doors!')
            chosen_door = None
    return chosen_door

def choices():
    amount_doors = int(input('Please enter the amount of doors in your problem '))
    amount_simulations = int(input('Please input the amount of simulations you would like to run'))
    switch_choice = input('do you want your simulation to switch doors or keep the first choice? (swap/keep) ').lower()
    return amount_doors, amount_simulations, switch_choice 

def monty_hall_random(num_doors, num_simulations, swap):
    wins = 0
    
    for _ in range(num_simulations):
        # Place the prize behind a random door
        prize_door = random_allocator(num_doors, num_doors, isRandom = True)
        
        # Contestant's initial choice
        initial_choice = random_allocator(num_doors, num_doors, isRandom = True)
        
        # Host opens all doors but a door that is neither the prize door nor the initial choice
        available_doors = set(range(1, num_doors + 1)) - {prize_door, initial_choice}
        
        if initial_choice == prize_door:
            unopened_door = random_allocator(num_doors, available_doors, isRandom = False)
        else:
            unopened_door = prize_door
        
        
        # The spirit of the monty hall problem is that if swap is chosen, the player has chosen
        # The only unopened door.
        if swap == True:
            final_choice = unopened_door
        elif swap == False:
            final_choice = initial_choice
        '''available_switches = {initial_choice, unopened_door}
        if available_switches:
            final_choice = random_allocator(num_doors, available_switches, isRandom = False)
        else:
            # If there are no available doors to switch to, stick with the initial choice
            final_choice = initial_choice'''
        
        # Check if the contestant wins
        if final_choice == prize_door:
            wins += 1

    return wins, num_simulations

def monty_hall_game(doors_count):
    
    win_count = 0
    loss_count = 0
    
    while True:
        prize_door = random_allocator(doors_count, doors_count, True)
        guess = input('Choose a door: ')
        available_doors = set(range(1, doors_count + 1)) - {prize_door, guess}
        if guess == prize_door:
            unopened_door = random_allocator(doors_count, available_doors, isRandom = False)
        else:
            unopened_door = prize_door
        choice = input(f'Monty opens all the doors except {unopened_door}. Would you like to stay or swap? ').lower()
        if choice == 'stay':
            guess = unopened_door
        if guess == prize_door:
            print('Congratulations! you won!')
            win_count = win_count + 1
        else:
            print('Loser!')
            loss_count = loss_count + 1
        again = input('Would you like to play again? (y/n). press t for your tally of results ').lower()
        if again == 'y':
            continue
        elif again == 'n':
            break
        elif again == 't':
            print(f'You have won {win_count} times and lost {loss_count} times')
        



# Example usage
'''print('Welcome to the three door simulator')
amount_doors = int(input('Please enter the amount of doors in your problem '))
amount_simulations = int(input('Please input the amount of simulations you would like to run'))
switch_choice = input('do you want your simulation to switch doors or keep the first choice? (swap/keep) ').lower()
if switch_choice == 'swap':
    swap = True
elif switch_choice == 'keep'
    swap = False



wins, total = monty_hall_random(amount_doors, amount_simulations, swap)
print(f"Wins: {wins}")
print(f"Total simulations: {total}")
print(f"Win rate: {wins/total:.2%}")'''

def menu():
    print('Welcome to the monty hall simulator!')
    print('Would you like to play the game yourself? or simulate games played?')
    selection = input('Enter your selection (Play/Simulate)').lower()
    if selection == 'play':
        doors_count = int(input('How many doors are in your game?'))
        monty_hall_game(doors_count)
    elif selection == 'simulate':
        amount_doors, amount_simulations, switch_choice = choices()

        if switch_choice == 'swap':
            swap = True
        elif switch_choice == 'keep':
            swap = False

        monty_hall_random(amount_doors, amount_simulations, swap)
        print(f"Wins: {wins}")
        print(f"Total simulations: {total}")
        print(f"Win rate: {wins/total:.2%}")

menu()
    