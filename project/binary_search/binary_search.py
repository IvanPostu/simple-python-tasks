import random


def generate_random_list():
    start = random.randint(0, 100)
    return list(range(start, 200, 2))


def split_list_in_two_sublist(a_list):
    """Split list in two sublists
    Args:
        -
    Returns:
        Tuple ( first_chunk, second_chunk )
    Raises:
        -
    """
    half = int(len(a_list) / 2) + len(a_list) % 2
    return (a_list[:half], a_list[half:])


def list_patentially_contain_a_value(list_, value):
    """Check if list patentially contain a value
    Args:
        list of numbers,
        value - number
    Returns:
        Boolean value
    Raises:
        -
    """
    first_elm = list_[0]
    last_elm = list_[len(list_) - 1]

    conditions = [
        first_elm < value and last_elm < value,
        first_elm > value and last_elm > value,
    ]

    return not any(conditions)


def binary_search(_list, search_val):
    """Do binary search
    Args:
        _list - list of numbers between rand and 200, step
    Returns:
        -
    Raises:
        -
    """
    temp_list = _list
    iteration_counter = 0

    while True:
        iteration_counter += 1
        print(f'\nIteration {iteration_counter}\nList: {temp_list}\n')

        if(len(temp_list) == 1):
            break
        (list_a, list_b) = split_list_in_two_sublist(temp_list)

        temp_list = list_a if list_patentially_contain_a_value(
            list_a, search_val) else list_b

    return True if temp_list[0] == search_val else False


def show_binary_search():
    while True:
        print('Enter a number between 100 and 200 :  ')
        search_val = int(input())
        _list = generate_random_list()
        if binary_search(_list, search_val):
            print(f'Your value {search_val} has been founded.')
        else:
            print(f'Your value {search_val} not found.')
        print('Try again? [y,n]: ')
        if(input() != 'y'):
            break
