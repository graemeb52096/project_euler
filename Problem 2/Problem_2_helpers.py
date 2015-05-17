__author__ = 'BatesG1996'

def get_fibonacci(max_value):
    """
    :param max_value: int
    :return: [list of numbers]

    Returns fibonacci sequence with values under max value

    >>> get_fibonacci(10)
    [1, 2, 3, 5, 8]

    >>> get_fibonacci(20)
    [1, 2, 3, 5, 8, 13]
    """
    sequence = []
    previous = 1
    current = 2
    sequence.append(previous)
    while current < max_value:
        sequence.append(current)
        x = current + previous
        previous = current
        current = x
    return sequence


def remove_odds_from_list(list_of_numbers):
    """
    :param list_of_numbers: [list of numbers]
    :return: [list of number]

    Removes odd numbers from a list of numbers

    >>> remove_odds_from_list([0, 1, 2, 3, 4, 5])
    [0, 2, 4]

    >>> remove_odds_from_list([10, 15, 20, 25, 30])
    [10, 20, 30]
    """
    output_list = []
    for number in list_of_numbers:
        if number % 2 == 0:
            output_list.append(number)
    return output_list