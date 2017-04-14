from random import randint

chances_count = 10
guessed_letter_count = 0

words = ['rabbit', 'football', 'laptop', 'paris', 'city', 'car', 'movie']

random_num = randint(0, len(words) - 1)
word_to_guess = words[random_num]
len_of_word_to_guess = len(word_to_guess)

result = []
for x in range(0, len_of_word_to_guess):
    result.append('_')
    print(result[x], end=' ')
print()

while chances_count > 0:
    letter = input('Guess: ')

    if letter in word_to_guess:
        for x in range(0, len_of_word_to_guess):
            if(word_to_guess[x] == letter):
                result.pop(x)
                result.insert(x, letter)
                guessed_letter_count += 1

        for x in range(0, len_of_word_to_guess):
            print(result[x], end=' ')
        print()
    else:
        print('Wrong letter')
        chances_count -= 1

    if guessed_letter_count == len_of_word_to_guess:
        break

if guessed_letter_count == len_of_word_to_guess:
    print('You WON !')
else:
    print('You LOSE!')
