import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            count = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[count] = letter
                count+=1
            print(self.word_guessed)
            self.num_letters -=1
            
        #break
            
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f'you have {self.num_lives} lives left.')
        

    def ask_for_input(self):
        # while self.num_lives > 0:
            guess = input("please input a single character: ")
        
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                #break
            elif len(guess) == 1 and guess.isalpha() and guess in self.list_of_guesses:
                print("You already tried that letter!")
                #break
            elif len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
                
    

def play_game(word_list):
    num_lives = 5          
    hang = Hangman(word_list, num_lives)
    while True:
        if hang.num_lives == 0:
            print("You lost!")
            break
        elif hang.num_letters > 0:
            hang.ask_for_input()
            print('num lives: ' ,hang.num_lives, 'num letters' , hang.num_letters)
        elif hang.num_lives != 0 and not hang.num_letters > 0:
            print('Congratulations. You won the game!')
            break
        

play_game(['apple', 'pear', 'banana', 'mango', 'strawberry'])