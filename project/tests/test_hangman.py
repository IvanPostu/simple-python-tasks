from hangman.Hangman import Hangman
import unittest
from unittest.mock import patch


class TestHangman(unittest.TestCase):

    @patch.object(Hangman, 'extract_random_word_from_file')
    def test_is_finalized(self, fake):
        fake.return_value = 'Hello'
        hangman = Hangman()
        hangman.generate_word()
        hangman.check_letter('H')
        hangman.check_letter('E')
        hangman.check_letter('L')
        hangman.check_letter('o')

        # test if is finalized
        assert hangman.is_finalized()

        fake.return_value = 'Bye'
        hangman.generate_word()
        hangman.check_letter('a')
        hangman.check_letter('b')
        hangman.check_letter('c')

        # test if is not finalized
        assert not hangman.is_finalized()

    @patch.object(Hangman, 'extract_random_word_from_file')
    def test_check_letter(self, fake):
        fake.return_value = 'Nature'
        hangman = Hangman()
        hangman.generate_word()

        assert not hangman.check_letter('H')
        assert not hangman.check_letter('Z')
        assert hangman.check_letter('a')
        assert hangman.check_letter('A')
        assert hangman.check_letter('E')
