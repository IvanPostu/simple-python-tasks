import os
from guess_the_number.guess_the_number import guess_the_number
from rock_paper_scissors_game.rock_paper_scissors_game import rock_paper_scissors_game
from sine_vs_cosine_graphic.sine_vs_cosine_graphic import sine_vs_cosine_graphic
from password_manager.password_manager import password_manager
from binary_search.binary_search import show_binary_search
from hangman.hangman import hangman_show


def main():
    msg = ('1 - to play guess the number,\n'
           '2 - to play rock paper scissors,\n'
           '3 - to see sine vs cosine graphic,\n'
           '4 - to use password generator\n'
           '5 - to show binary search\n'
           '6 - to play hangman\n'
           'something else for exit\n'
           )

    while True:
        os.system('clear')
        print(msg)
        user_input = input()[0]
        if(user_input == '1'):
            guess_the_number()
            continue
        if user_input == '2':
            rock_paper_scissors_game()
            continue
        if user_input == '3':
            sine_vs_cosine_graphic()
            continue
        if user_input == '4':
            password_manager()
            continue
        if user_input == '5':
            show_binary_search()
            continue
        if user_input == '6':
            hangman_show()
            continue
        break


if __name__ == '__main__':
    main()
