import random

solution = []
user_guess = []
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
        letter_guess = input("Guess a letter? ").lower()
        if letter_guess in solution:
            #these loops allow for multiples of the same letter
            for idx in range(len(solution)):
                if solution[idx] == letter_guess:
                    user_guess[idx] = letter_guess
        else:
            tries -= 1
            print(f"You have {tries} remaining")
    #when loop ends determines if you won or lost
    if '_' in user_guess:
        print("You Lose! Try Again")
    else:
        print("You Won!")


def play_game(file):
    with open(file) as open_file:
        read_file = open_file.read()
    chosen_word = choose_word(read_file)
    prepare_game(chosen_word)
    start_game(tries_left)

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
