from hangman.Hangman import Hangman


def hangman_round(attempts, hangman):
    loop_times = attempts

    hangman.generate_word()
    while loop_times >= 0:
        print(f'\nYou have {loop_times} attempts left')
        print('Enter letter or word: ')
        user_input = input()
        is_letter = len(user_input) == 1

        if is_letter:
            hangman.check_letter(user_input)
        else:
            hangman.check_word(user_input)

        if hangman.is_finalized():
            return True
        else:
            print(f'Current status: {hangman.current_word_status}')

        loop_times -= 1

    return False


def hangman_show():
    while True:
        hangman = Hangman()
        user_win = hangman_round(5, hangman)
        if user_win:
            print('Congratulations you won')
        else:
            print(f'You lose, correct word is {hangman.current_word}')
        print('Try again? [y,n]: ')
        if(input() != 'y'):
            break
