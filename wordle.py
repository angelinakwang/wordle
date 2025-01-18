import random
#Description: This is the game of Wordle. The user has six attempts to guess a random five-letter word. After each valid input, the game provides feedback that indicates which letters are correct and in the correct position (green letters) and which letters are correct but in the wrong position (yellow letters).
print ('Welcome to Wordle!')
print ('Type a 5 letter word and hit enter to play!')

word_bank = ['abort', 'bound', 'bread', 'cable', 'chest', 'dopey', 'drown', 'enemy', 'filth', 'glare', 'murky', 'owing', 'pause', 'quail', 'racer', 'ranch', 'skier', 'snare', 'twine', 'usage', 'vital', 'yacht']

def random_word():
    return random.choice(word_bank)

#Presents the wordle board to the user on the screen
def display_wordle(user_input_list):
    num_guesses = len(user_input_list)
    for y in range(len(user_input_list)):
            print(user_input_list[y])
    x = 6 - num_guesses 
    x = 7 - x 
    while x <= 6:
        print (str(x) +  ' _ _ _ _ _')
        x = x + 1
    return

# Input - Guess - String, the User-Provided Guess / Word - The Answer to the Wordle
# Output - False - Representing an Invalid Guess 
#           OR Space_Word Representing the final string of the Guess with any color changes and formatting changes
def check_word(guess, word):
    if len(guess) != 5:
        print("Please put a 5 letter word.")
        return False
    if guess.isalpha() == False:
        print("No number/special characters/spaces please.")
        return False
    guess_letters =  ["_","_","_","_","_"] #list that stores indvidual characters of the guess with color changes
    space_word = "" #string representing the characters that will be printed
    copy_word = word
    for i in range(5):
        if guess[i] == copy_word[i]:
            guess_letters[i] = ('\033[92m' + guess[i] + '\033[0m') #ANSI Escape Code to make string green
            copy_word = copy_word.replace(guess[i], ' ', 1) 
    for i in range(5):
        if guess[i] in copy_word and guess_letters[i] == "_":
            guess_letters[i] = '\033[93m' + guess[i] + '\033[0m'#ANSI Escape Code to make string yellow
            copy_word = copy_word.replace(guess[i], ' ', 1) 
        elif guess_letters[i] == "_":
            guess_letters[i]=(guess[i])
        space_word = space_word + guess_letters[i] + " "
    return space_word


def attempt(user_input_list, word, num_guesses):
    user_input = input("Enter your guess: ").upper()    #Prompts user for user input 
    if(check_word(user_input, word) != False):
        user_input_list.append(str(num_guesses + 1) + " " + check_word(user_input, word)) #Add to the list of user inputs
    if user_input == word:
        display_wordle(user_input_list)
        print("Congratulations! The word was " + word + " and you guessed it in " + str(num_guesses+1) + " attempts!")
        return True
    if num_guesses == 5:    #Ends the game after 6 user attempts
        display_wordle(user_input_list)
        print("Better luck next time! The word was " + word + "!")
        return False
    return False


def play_wordle():
    user_input_list = []    #A list to keep track of user inputs
    word = random.choice(word_bank).upper()
    correct = False
    while len(user_input_list) < 6:
        display_wordle(user_input_list)
        correct = attempt(user_input_list, word, len(user_input_list))
        if(correct == True):
            break


if __name__ == "__main__":
    play_wordle()