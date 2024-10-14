from random import choice


def choose_word(words):
    word_to_find = choice(words)
    return word_to_find


def initialize_hangman_spaces(word):
    spaces = []
    for i in range(len(word)):
        space = '_'
        spaces.append(space)
    return spaces


def ask_for_letter():
    letter = input('Introduce a letter: ')
    while not (letter.isalpha()) or (len(letter) != 1):
        print('Error. You have to introduce a letter.')
        letter = input('Introduce a letter: ')
    return letter


def check_letter(word_to_find, letter, wrong_letters, right_letters, lives, spaces):
    if letter in wrong_letters or letter in right_letters:
        print('You have chosen that letter earlier. Choose another one.')
        return lives, spaces

    else:
        if letter in word_to_find:
            print('Congratulations, your letter is correct.')
            right_letters.append(letter)
            print('Right letters:', right_letters)
            for i in range(len(word_to_find)):
                if word_to_find[i] == letter:
                    spaces[i] = letter
            if ''.join(spaces) == word_to_find:
                print('Congratulations. You find the word.')
                exit()
            print('Current word:', ' '.join(spaces))

        else:
            print('Wrong letter. Keep trying.')
            wrong_letters.append(letter)
            print('Wrong letters: ', wrong_letters)
            lives -= 1
            print(f'You lost a life. You have {lives} lives left.')
            if lives == 0:
                print('Oh, you do not have more lives. The game is over.')
    return lives, spaces


if __name__ == "__main__":

    words = ['casa', 'tiburon', 'pescado', 'peliculas', 'libelula']
    wrong_letters = []
    right_letters = []
    lives = 6

    word_to_find = choose_word(words)
    spaces = initialize_hangman_spaces(word_to_find)
    print(spaces)

    while lives != 0:
        letter = ask_for_letter()
        lives, spaces = check_letter(word_to_find, letter, wrong_letters, right_letters, lives, spaces)
