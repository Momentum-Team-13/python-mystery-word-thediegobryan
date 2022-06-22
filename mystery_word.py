import random

solution = []
user_guess = []
available_guesses = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

tries_left = 8

def choose_word(words):
    difficulty = input("Choose a Difficulty.\neasy (4-6 letters) | normal (6-8 letters) | hard (8+ letters) \n")
    #verifies user difficulty is valid
    while difficulty != 'easy' and difficulty!= 'normal' and difficulty != 'hard':
        print('Not an option, pick again')
        difficulty = input("Choose a Difficulty.\neasy (4-6 letters) | normal (6-8 letters) | hard (8+ letters) \n")
    
    list_of_words = words.split()
    if difficulty == 'easy':
        for word in list_of_words.copy():
            if len(word) > 6:
                list_of_words.remove(word)
    elif difficulty == 'normal':
        for word in list_of_words.copy():
            if len(word) > 8 or len(word) < 6:
                list_of_words.remove(word)
    elif difficulty == 'hard':
        for word in list_of_words.copy():
            if len(word) < 8:
                list_of_words.remove(word)
    
    return random.choice(list_of_words)

def prepare_game(word):
    word_list = list(word)
    for char in word_list:
        solution.append(char)
        user_guess.append("_")
    
def start_game(tries):
    while tries > 0 and '_' in user_guess:
        print(" ".join(user_guess))
        print(f"Availble Guesses: {available_guesses}")
        letter_guess = input("Guess a letter? ").lower()
        if letter_guess in available_guesses:
            index = available_guesses.index(letter_guess)
            available_guesses[index] = '❌'

            if letter_guess in solution:
            #these loops allow for multiples of the same letter
                for idx in range(len(solution)):
                    if solution[idx] == letter_guess:
                        user_guess[idx] = letter_guess
            else:
                tries -= 1
                print(f"You have {tries} tries remaining")
                
        else:
            print("Invalid guess. Guess Again")

    #when loop ends determines if you won or lost
    if '_' in user_guess:
        print(f"You Lose! The correct word was {(''.join(solution))}.")
    else:
        print(f"{(''.join(solution))} is the Word! You Won!")


def play_game(file):
    with open(file) as open_file:
        read_file = open_file.read()
    
    game_is_running = 'yes'
    while game_is_running == 'yes':
        chosen_word = choose_word(read_file)
        prepare_game(chosen_word)
        start_game(tries_left)

        game_is_running = input("Do you want to play again? yes or no \n")
        while game_is_running != 'yes' and game_is_running != 'no':
            print('Not an option, pick again')
            game_is_running = input("Do you want to play again? yes or no \n")

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Mystery word game')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
