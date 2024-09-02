import math
length  = int(input("How many terms would you like? "))
sequence = []
term = 1
count = 1
while length:
    if isinstance(length, int) and length >= 0:
        if length == 1:
          sequence = [1]
          print(sequence)
        elif length == 2:
          sequence = [1, 1]
          print(sequence)
        else:
            sequence = [1, 1]
            while len(sequence) < length:
                next_term = sequence[count] + sequence[count-1]
                sequence.append(next_term)
                count = count + 1
            print(sequence)
        length = int(input("How many terms woulf you like? "))
    else:
        print("Invalid Length")
        length = int(input("How many terms would you like? "))
