# Hangman

1. [ Description. ](#desc)
2. [ Usage. ](#usage)

<a name="desc"></a>

## 1. Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

<a name="usage"></a>

## 2. Usage

On milestone_3.py there are two functions created.

1. check_guess - this takes in a letter that will check if the letter is in the word
2. ask_for_input - this method asks the user for a letter, validates the input in case of an invalid character or multiple characters, and then calls the check_guess method.

milestone_4.py is a class called Hangman.

1. Constructor

   - Parameters:
     word_list: list - a list of words for the computer to chose from.
     num_lives: int - number of attempts at finding the word (default is set to 5).

2. Attributes:

   - word: string - The word to be guessed, picked randomly from the word_list.
   - word*guessed: list - A list of the letters of the word, with * for each letter not yet guessed. For example, if the word is 'apple', the word*guessed list would be ['*', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
   - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
   - list_of_guesses: list - A list of the guesses that have already been tried. Set to an empty list initially

3. Methods:
   - check_guess: Passes the guess to the method as a parameter. Converts the guessed letter to lower case, checks if the user's guess is a letter in the hidden word, and updates the amount of lives accordingly.
   - ask_for_input: Validates the user's guess to ensure that it is a single letter and not a number or special character. It also ensures that the guess is not the same as a previous guess.
