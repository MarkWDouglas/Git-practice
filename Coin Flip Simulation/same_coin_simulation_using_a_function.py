import random

def flip_the_coin(number_of_flips):
    S = ['H','T'] # the coin's sample space
    samples = []  # will store the results of the flips 

    for i in range(number_of_flips):
        flip = random.choice(S)
        samples.append(flip)

    # now that we are done, summarise
    num_heads = samples.count('H')
    num_tails = samples.count('T')
    print(f"Heads: {num_heads}, Tails {num_tails}")
    # from here you can calculate relative frequencies

for count in range(10): # call the function x times
    flip_the_coin(1000) # call the function to flip coin 1000 times