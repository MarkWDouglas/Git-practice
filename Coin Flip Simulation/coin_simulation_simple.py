import random

S = ['H','T'] # the coin's sample space
samples = []  # will store the results of the flips 

number_of_flips = 100

for i in range(number_of_flips):
    flip = random.choice(S)
    samples.append(flip)

# now that we are done, summarise
num_heads = samples.count('H')
num_tails = samples.count('T')
print(f"Heads: {num_heads}, Tails {num_tails}")
# from here you can calculate relative frequencies