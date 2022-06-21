solution = []
user_guess = []
tries_left = 8

def prepare_game(word):
    word_list = list(word)
    word_list.pop()
    for char in word_list:
        solution.append(char)
        user_guess.append("_")
    
def start_game(tries):
    print(user_guess)
    while tries > 0:
        letter_guess = input("Guess a letter? ").lower()
        if letter_guess in solution:
            print("This letter is in the word")
        else:
            tries -= 1
            print(f"You have {tries} remaining")
        



def play_game(file):
    with open(file) as open_file:
        read_file = open_file.read()

    prepare_game(read_file)

    start_game(tries_left)

    print(solution, user_guess)




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

# - [ ] READ a word (test-word.txt)
# - [ ] Initialize solution list [C,A,T] that splits up each letter
# - [ ] Initialize user input list with blanks [_ , _, _] based on length of solution word. (len(solution_word))
# - [ ] Ask user for a letter (input(“what is your guess”)
#     - [ ] Compare user input with solution list like we did with stop words in the word_frequency assignment
#         - [ ] If user input is in the solution then replace user input list blank with the letter guessed. [C, _, _]
#         - [ ] Else say user guess is wrong and to guess again

