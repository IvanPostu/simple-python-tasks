import secrets
import random


class PasswordGenerator:
    __symbols = '$_-#@'
    __letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    __numbers = '0123456789'

    def __init__(self, letters_count, numbers_count, symbols_count):
        self.__letters_count = letters_count
        self.__numbers_count = numbers_count
        self.__symbols_count = symbols_count

    def generate(self):
        """Generate random password.
        Args:
            -
        Returns:
            String generated password
        Raises:
            -
        """
        password = ''
        for i in range(self.letters_count):
            if(random.randint(0, 1) == 0):
                password += secrets.choice(
                    PasswordGenerator.__letters_lowercase)
            else:
                password += secrets.choice(
                    PasswordGenerator.__letters_lowercase.upper())
        for i in range(self.numbers_count):
            password += secrets.choice(PasswordGenerator.__numbers)
        for i in range(self.symbols_count):
            password += secrets.choice(PasswordGenerator.__symbols)
        return self.__permute_text(password, random.randint(10, 20))

    def __permute_text(self, text, loop_count):
        """Simple permutation recursive method
        Args:
            text - required, string to be permuted
            loop_count - required, how many times need to permute string
        Returns:
            String permutated string
        Raises:
            -
        """
        if(loop_count == 0):
            return text

        new_str = ''
        for c in text:
            new_str = c + new_str if random.randint(0, 1) == 0 else new_str + c

        return self.__permute_text(new_str, loop_count - 1)

    @property
    def pass_length(self):
        return self._pass_length

    @property
    def letters_count(self):
        return self.__letters_count

    @property
    def numbers_count(self):
        return self.__numbers_count

    @property
    def symbols_count(self):
        return self.__symbols_count
