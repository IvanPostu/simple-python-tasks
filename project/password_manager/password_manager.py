import os
from password_manager.PasswordGenerator import PasswordGenerator


def user_view():
    """Generate random password.
    Args:
        -
    Returns:
        Tuple ( letters_count, numbers_count, symbols_count )
    Raises:
        -
    """
    while True:
        try:
            print('Enter letters count: ')
            letters_count = int(input())
            print('Enter numbers count: ')
            numbers_count = int(input())
            print('Enter symbols count: ')
            symbols_count = int(input())

            conditions = [
                letters_count <= 0,
                numbers_count <= 0,
                symbols_count <= 0,
            ]

            if any(conditions):
                raise ValueError()

            return (letters_count, numbers_count, symbols_count)
        except ValueError:
            os.system('clear')
            print('Input is not valid !!!\n\n')
            continue


def password_manager():
    while True:
        (letters_count, numbers_count, symbols_count) = user_view()

        if(letters_count + numbers_count + symbols_count < 6):
            os.system('clear')
            print('The password should be a minimum of 6 characters long.\n\n')
            continue

        pass_gen = PasswordGenerator(
            letters_count, numbers_count, symbols_count)
        generated_password = pass_gen.generate()
        print('Generated password: ' + generated_password)
        break
