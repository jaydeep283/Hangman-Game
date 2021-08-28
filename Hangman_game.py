# Hangman game which lets user to predict the letters from the random word chosen by program.

#For choosing word randomly
import random

#Path for text file containing all possible words.
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Loading the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    sw_len = len(secretWord)
    lg_len = len(lettersGuessed)
    corr_guess = 0
    for x in secretWord:
        if x in lettersGuessed:
            corr_guess = corr_guess + 1
    if corr_guess == sw_len:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    g_str = ''
    for x in secretWord:
        if x in lettersGuessed:
            g_str = g_str + x
        else:
            g_str = g_str + '_ '
    return g_str


import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avl_lett = ''
    for x in string.ascii_lowercase:
        if x not in lettersGuessed:
            avl_lett = avl_lett + x
    return avl_lett


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Start of an interactive game of Hangman.

    * At the start of the game, it shows how many letters are there in secret word.

    * Asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, it displays to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    print("Welcome to the game Hangman!")
    len_sec_word = len(secretWord)
    print("I am thinking of a word that is", len_sec_word, "letters long.")
    print("________________________")

    tot_guesses = 8  #Tracks the life i.e how many more times user can guess incorrect letter
    mistakes_Made = 0
    lettersGuessed = []  #Stores the letters guessed so far by the user.
    avl_letters = getAvailableLetters(lettersGuessed)

    while tot_guesses > 0:
        print("You have", tot_guesses, "guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess_lowercase = guess.lower()

        if guess_lowercase in secretWord and guess_lowercase not in lettersGuessed:
            lettersGuessed.append(guess_lowercase)
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
        elif guess_lowercase in secretWord and guess_lowercase in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess_lowercase in lettersGuessed:
                print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess_lowercase)
                tot_guesses = tot_guesses - 1

        print("________________________")

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break

    if not isWordGuessed(secretWord, lettersGuessed):
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

# Start of the main program.
# Chooses random word and passes it to hangman function to start the game.
secretWord = chooseWord(wordlist)
hangman(secretWord)
