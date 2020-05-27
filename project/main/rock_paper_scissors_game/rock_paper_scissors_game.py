import random
import os
from rock_paper_scissors_game.Variants import Variants


def question_for_user():
    """
      Show message to user.
    """
    print('Please enter a number for the desired variant:')

    for v in Variants:
        print(f'{v.value} -> to choose {v.name}.')

    print('If you wanna to go out, please enter any character\n')


def handle_user_input(user_raw_input):
    """
      Handle user input

      Args:
          user_raw_input: User input string
      Returns:
          string mesage
      Raises:
          -1 if string parse throws exception
    """
    try:
        return int(user_raw_input)
    except ValueError:
        return -1


def bot_generate_variant():
    """
      Generate rock_paper_scissors variant using random

      Args:
          -
      Returns:
          Variant
      Raises:
          -
    """
    rand_int = random.randint(Variants.min_val(), Variants.max_val())
    return Variants(rand_int)


def game_action(bot_variant, user_variant):
    """
      Win or lose conditions

      Args:
          -
      Returns:
          string message: user win or lose or draw
      Raises:
          -
    """

    user_win_rules = [
        bot_variant == Variants.PAPER and user_variant == Variants.SCISSORS,
        bot_variant == Variants.ROCK and user_variant == Variants.PAPER,
        bot_variant == Variants.SCISSORS and user_variant == Variants.ROCK
    ]

    if(bot_variant.value == user_variant.value):
        return f'DRAW, bot select {bot_variant.name}, you select {user_variant.name}'
    if any(user_win_rules):
        return f'Congratulations, you WIN, bot select {bot_variant.name}'
        + f', you select {user_variant.name}'
    else:
        return f'Alas, you LOST, bot select {bot_variant.name}, you select {user_variant.name}'


def rock_paper_scissors_game():
    while True:
        question_for_user()
        user_int_value = handle_user_input(input())
        if(not user_int_value in Variants._value2member_map_):
            break
        user_variant = Variants(user_int_value)
        bot_variant = bot_generate_variant()
        game_message = game_action(bot_variant, user_variant)
        os.system('clear')
        print(game_message)
