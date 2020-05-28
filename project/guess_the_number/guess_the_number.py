import random


def compare_with_random(user_num):
    """
      Args:
          user_num: entered number by user
      Returns:
          string mesage
      Raises:
          -
    """
    rand_val = random.randint(0, 20)
    print(f'The generated value is: {rand_val}')
    if user_num > rand_val:
        return 'The entered number is greater than the generated.'
    if(user_num < rand_val):
        return 'The entered number is less than the generated.'
    if(user_num == rand_val):
        return 'The entered number is equal to the generated.'


def guess_the_number():
    while True:
        print('Enter a number between 0 and 20 ')
        user_input_num = 0

        try:
            user_input_num = int(input())
        except ValueError:
            print('Error - input is not a number. Please enter a number between 0 and 20')
            continue

        if user_input_num < 0 or user_input_num > 20:
            print('Entered number is not valid. Please enter a number between 0 and 20. ')
            continue

        print(compare_with_random(user_input_num))
        print('Do you want it again? [y/n] ')
        if input() != 'y':
            break
