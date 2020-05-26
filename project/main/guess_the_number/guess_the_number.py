import random

def is_int_convertable(val):
  try:
    int(val)
    return True
  except ValueError:
    return False

def compare_with_random(user_num):
  rand_val = random.randint(0, 20)
  print(f'The random value is: {rand_val}')
  if user_num > rand_val:
    return 'The entered number is greater than the generated.'
  if(user_num < rand_val):
    return 'The entered number is less than the generated.'
  if(user_num == rand_val):
    return 'The entered number is equal to the generated.'

def guess_the_number():
  while True:
    print('Enter a number between 0 and 20 ')
    user_input = input()
    user_input_num = -1

    if is_int_convertable(user_input):
      user_input_num = int(user_input)

    while user_input_num < 0 or user_input_num > 20:
      print('Entered number is not valid. Please enter a number between 0 and 20 ')
      user_input = input()
      if is_int_convertable(user_input):
        user_input_num = int(user_input)

    print(compare_with_random(user_input_num))
    print('Do you want it again? [y/n] ')
    if input() != 'y':
      break
