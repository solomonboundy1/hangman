import random

word_list = ['apple','banana','orange','mango','pineapple']
word = random.choice(word_list)
guess = input("please input a single character")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

if __name__ == '__main__':
    print(word_list)
    print(word)