from hangman.Hangman import Hangman


def hangmen_show():
    hangman = Hangman()
    hangman.generate_word()
    hangman.check_letter('a')
    hangman.check_letter('b')
    hangman.check_letter('c')
    hangman.check_letter('d')
    hangman.check_letter('e')
    hangman.check_letter('f')
    z = hangman.is_finalized()
    a = 1
