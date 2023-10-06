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
