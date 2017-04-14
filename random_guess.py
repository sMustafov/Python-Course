from random import randint

input_str = input()
not_guessed = True
my_number = randint(1,9)

while not_guessed:
    if my_number == int(input_str):
        not_guessed = False
    else:
        print('You dont guess, please continioue')
        input_str = input()

print('Yes you guess, the random number was {}'.format(my_number))


