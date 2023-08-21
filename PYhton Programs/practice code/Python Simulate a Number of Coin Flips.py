# import random module to use random.randint
import random


# define function with name and number of flips argument
def heads_tails(number_of_flips):
    # count variables to hold tally count (will use with addition compound assignment operator)
    tails_count = 0
    heads_count = 0
    # use loop to flip coin specified number of times using number passed when function called
    for i in range(number_of_flips):
        # each time through loop or for each coin flip generate random integer of 1 or 2
        rand = random.randint(1, 2)
        # if random integer 1 this will represent a tail and add 1 to tails count
        if rand == 1:
            tails_count += 1
            # print tails tally as you go
            print(tails_count, 'tails')
        # if random integer is 2 this will represent a head and add 1 to heads count
        else:
            heads_count += 1
            # print heads tally as you go
            print(heads_count, 'heads')
    # print final tally count for all coin flips
    print('tails', tails_count)
    print('heads', heads_count)


# call function to simulate n coin flips
heads_tails(10)
