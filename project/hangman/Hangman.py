import random


class Hangman:

    @staticmethod
    def extract_random_word_from_file():
        f = open("sowpods.txt", 'r')
        total_lines = sum(1 for line in f)
        f.seek(0)
        rand_line = random.randint(0, total_lines - 1)
        iter = 0
        result = ''
        for s in f:
            if (iter == rand_line):
                result = s
                break
            iter += 1
        f.close()
        return result

    def __init__(self):
        """
        Args:
            -
        Returns:
            -
        Raises:
            -
        """
        f = open("sowpods.txt", 'r')
        self.__total_lines = sum(1 for line in f)
        self.__current_status = ''
        self.__current_word = ''
        f.close()

    def generate_word(self):
        """
        Args:
            -
        Returns:
            -
        Raises:
            -
        """
        self.__current_word = self.__current_status = ''
        self.__current_word = Hangman.extract_random_word_from_file().lower().strip()
        for c in self.__current_word:
            self.__current_status += '*'

    def check_letter(self, letter):
        """
        Args:
            letter - check if this letter exists in self.__current_word
        Returns:
            True if found at least one letter in word
            False if not found
        Raises:
            -
        """
        letter = letter.lower()
        word_len = len(self.__current_word)
        new_str_status_arr = list(self.__current_status)
        return_value = False
        while(word_len != 0):
            word_len -= 1
            if self.__current_word[word_len] == letter:
                return_value = True
                new_str_status_arr[word_len] = letter

        self.__current_status = ''.join(new_str_status_arr)

        return return_value

    def check_word(self, word):
        """
        Args:
            word - check if this word is equal with self.__current_word
        Returns:
            True if is equal
            False if is not equal
        Raises:
            -
        """
        formatted_word = word.lower().strip()
        if formatted_word == self.__current_word:
            self.__current_status = self.__current_word = formatted_word
            return True
        else:
            return False

    def is_finalized(self):
        return not any(i == '*' for i in self.__current_status)

    @property
    def current_word_status(self):
        return self.__current_status

    @property
    def current_word(self):
        return self.__current_word
