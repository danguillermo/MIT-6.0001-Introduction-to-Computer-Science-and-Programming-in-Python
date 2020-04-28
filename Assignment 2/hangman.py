# Problem Set 2, hangman.py
# Name: Daniel Guillermo
# Collaborators: Daniel Guillermo
# Time spent: About 4 hours

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
    i=0
    for letter_S in secret_word:
        for letter_G in letters_guessed:
            if letter_S == letter_G:
                i+=1
                break
            
    return len(secret_word) == i



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_shown= []
    counter=0
    for letter_S2 in secret_word:


        for letter_G2 in letters_guessed:
            if letter_S2 == letter_G2:
                word_shown.append(letter_S2+' ')
                break
            else:
                counter+=1
                
        if counter == len(letters_guessed):
            word_shown.append('_ ')
            counter=0
        else:
            counter=0
            
    return "".join(word_shown)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=list(string.ascii_lowercase)
    for letter_all in string.ascii_lowercase:
        for letter_G3 in letters_guessed:
            if letter_all == letter_G3:
                available_letters.remove(letter_G3)
    
    return " ".join(available_letters)
    
def unique_letters(word):
    '''
    word: a string of letters
    returns: number of unique letters in word
    '''
    unique=[]
    for letter in word:
        if not(letter in unique):
            unique.append(letter)
    return len(unique)

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
    guess=6
    warning=3
    available_letters=list(string.ascii_lowercase)
    
    print('Welcome to Hangman TM!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('You have', warning,'warnings left')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You have', guess,'guesses left')
    print('Available letters:'," ".join(available_letters))
    
    all_letters_guessed=[]
    while guess > 0:
        if not all_letters_guessed:
            letter_guessed=str(input('Please enter a letter: '))
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('You have', guess,'guesses left')
            print('Available letters:',get_available_letters(all_letters_guessed))
            letter_guessed=str(input('Please enter a letter: '))
            
        if letter_guessed.isalpha():
            if len(letter_guessed) == 1:
                
                if letter_guessed in all_letters_guessed:
                    
                    if warning > 0:
                        warning -=1
                        print('Opsie! You\'ve guessed that letter already.',
                              'You have now',warning,'warnings.')
                        print(get_guessed_word(secret_word, all_letters_guessed))
                    else:
                        guess -=1
                        print('Opsie! You\'ve guessed that letter already.',
                              'You have no warnings. So, you have',
                              guess,'guesses')
                        print(get_guessed_word(secret_word, all_letters_guessed))
                        
                else:
                    all_letters_guessed.append(letter_guessed.lower())
                    if letter_guessed.lower() in secret_word:
                        print('Good guess!')
                        print('The word looks like:',get_guessed_word(secret_word, all_letters_guessed))
                    else:
                        
                        if letter_guessed.lower() in 'aeiou':
                            guess -=2
                            print('That letter is not in my word:',get_guessed_word(secret_word, all_letters_guessed))
                        else:
                            guess -=1
                            print('That letter is not in my word:',get_guessed_word(secret_word, all_letters_guessed))

            else:
                print('Please enter only one letter at a time.')
                
        else:
            if warning >= 1:
                warning-=1
                print('You have entered an invalid character. You have',
                      warning,'wanings left')
            elif warning == 1:
                warning-=1
                print('You have entered an invalid character. You have no',
                      'wanings left. You will be penalized with a guess if you',
                      'try any funny bussiness again.')
            else:
                guess-=1
                print('I warned you 3 times! You have',guess,'guesses left')
        
        if is_word_guessed(secret_word, all_letters_guessed):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Congratulations! You\'ve won.')
            print('Your total socre is:',guess*unique_letters(secret_word))
            break
    if guess < 1:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Sorry, you ran out of guesses. The word was',secret_word+'.')
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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
   
    my_word_together= my_word.replace(' ','')
    
    if len(my_word_together) != len(other_word):
        return False
    else:
        letter_count_other=[]
        for letter in other_word:
            letter_count_other.append(other_word.count(letter))
        i=0   
        for letter in my_word_together:   
            if letter.isalpha():
                if (my_word_together[i] == other_word[i]) and (letter_count_other[i] == my_word_together.count(letter)):
                    True
                else:
                    return False
            i+=1
            
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
    matching_words=[]
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matching_words.append(word)
    if not matching_words:
        print('No Matches found')
    return ' '.join(matching_words)



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
    guess=6
    warning=3
    available_letters=list(string.ascii_lowercase)
    
    print('Welcome to Hangman TM!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('You have', warning,'warnings left')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You have', guess,'guesses left')
    print('Available letters:'," ".join(available_letters))
    
    all_letters_guessed=[]
    while guess > 0:
        if not all_letters_guessed:
            letter_guessed=str(input('Please enter a letter: '))
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('You have', guess,'guesses left')
            print('Available letters:',get_available_letters(all_letters_guessed))
            letter_guessed=str(input('Please enter a letter: '))
            
        if letter_guessed.isalpha():
            if len(letter_guessed) == 1:
                
                if letter_guessed in all_letters_guessed:
                    
                    if warning > 0:
                        warning -=1
                        print('Opsie! You\'ve guessed that letter already.',
                              'You have now',warning,'warnings.')
                        print(get_guessed_word(secret_word, all_letters_guessed))
                    else:
                        guess -=1
                        print('Opsie! You\'ve guessed that letter already.',
                              'You have no warnings. So, you have',
                              guess,'guesses')
                        print(get_guessed_word(secret_word, all_letters_guessed))
                        
                else:
                    all_letters_guessed.append(letter_guessed.lower())
                    if letter_guessed.lower() in secret_word:
                        print('Good guess!')
                        print('The word looks like:',get_guessed_word(secret_word, all_letters_guessed))
                    else:
                        
                        if letter_guessed.lower() in 'aeiou':
                            guess -=2
                            print('That letter is not in my word:',get_guessed_word(secret_word, all_letters_guessed))
                        else:
                            guess -=1
                            print('That letter is not in my word:',get_guessed_word(secret_word, all_letters_guessed))

            else:
                print('Please enter only one letter at a time.')
                
        elif letter_guessed == '*':
            print('Posible word matches are: ')
            print(show_possible_matches(get_guessed_word(secret_word, all_letters_guessed)))
        else:
            if warning >= 1:
                warning-=1
                print('You have entered an invalid character. You have',
                      warning,'wanings left')
            elif warning == 1:
                warning-=1
                print('You have entered an invalid character. You have no',
                      'wanings left. You will be penalized with a guess if you',
                      'try any funny bussiness again.')
            else:
                guess-=1
                print('I warned you 3 times! You have',guess,'guesses left')
        
        if is_word_guessed(secret_word, all_letters_guessed):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Congratulations! You\'ve won.')
            print('Your total socre is:',guess*unique_letters(secret_word))
            break
    if guess < 1:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Sorry, you ran out of guesses. The word was',secret_word+'.')
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)