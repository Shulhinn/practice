# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_in_word = list(set(list(secret_word)))
    for letter in letters_in_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = []
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word.append(secret_word[i])
        else:
            word.append('_ ')
    return ''.join(word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    if len(letters_guessed) == 0:
        return string.ascii_lowercase
    available_letters = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters.append(letter)
    return ''.join(available_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have {} warnings left.".format(warnings_left))
        print("You have {} guesses left".format(guesses_left))
        print("Available letters: {}".format(get_available_letters(letters_guessed)))
        letter = str.lower(input("Please guess a letter: "))
        if not letter.isalpha() or len(letter) > 1:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings_left,
                                                                                               get_guessed_word(
                                                                                                   secret_word,
                                                                                                   letters_guessed)))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have {} guesses left: {}".format(guesses_left,
                                                                                              get_guessed_word(
                                                                                                  secret_word,
                                                                                                  letters_guessed)))
            continue
        if letter in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(warnings_left,
                                                                                                       get_guessed_word(
                                                                                                           secret_word,
                                                                                                           letters_guessed)))
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have {} guesses left: {}".format(guesses_left,
                                                                                                      get_guessed_word(
                                                                                                          secret_word,
                                                                                                          letters_guessed)))
            continue
        letters_guessed.append(letter)
        if letter not in secret_word:
            guesses_left -= 1
            print("Oops! That letter is not in my word:".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_left * len(set(list(secret_word)))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(total_score))
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_wo_spaces = my_word.strip().replace(' ', '')
    letters_that_was_in_other_word = []
    if len(my_word_wo_spaces) != len(other_word):
        return False
    for i in range(len(my_word_wo_spaces)):
        if my_word_wo_spaces[i] == '_':
            letters_that_was_in_other_word.append(other_word[i])
            continue
        if my_word_wo_spaces[i] != other_word[i]:
            return False
        if my_word_wo_spaces[i] == other_word[i] and my_word_wo_spaces[i] in letters_that_was_in_other_word:
            return False
        letters_that_was_in_other_word.append(other_word[i])
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matched_words = [word for word in wordlist if match_with_gaps(my_word, word)]
    if len(matched_words) == 0:
        return "No matches found"
    else:
        return ' '.join(matched_words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have {} warnings left.".format(warnings_left))
        print("You have {} guesses left".format(guesses_left))
        print("Available letters: {}".format(get_available_letters(letters_guessed)))
        letter = str.lower(input("Please guess a letter: "))
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if letter == '*':
            print("Possible word matches are: {}".format(show_possible_matches(guessed_word)))
        if not letter.isalpha() or len(letter) > 1:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings_left,
                                                                                               guessed_word))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have {} guesses left: {}".format(guesses_left,
                                                                                              guessed_word))
            continue
        if letter in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(warnings_left,
                                                                                                       guessed_word))
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have {} guesses left: {}".format(guesses_left,
                                                                                                      guessed_word))
            continue
        letters_guessed.append(letter)
        if letter not in secret_word:
            guesses_left -= 1
            print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_left * len(set(list(secret_word)))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(total_score))
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
