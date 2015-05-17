def get_multiples_of(multiple, max):
    """
    :param multiple: number
    :param max: int
    :return: list[]
    Returns multiples of five that are below the max

    >>> get_multiples_of(5, 10)
    [5]

    >>> get_multiples_of(3, 20)
    [3, 6, 9, 12, 15, 18]

    >>> get_multiples_of(5, 25)
    [5, 10, 15, 20]
    """
    x = multiple
    multiples_of = []
    while x < max:
        multiples_of.append(x)
        x += multiple
    return multiples_of

def remove_multiples_of(multiple, numbers):
    """
    :param multiple: Number
    :param numbers: list[]
    :return: list[]

    Given a list of numbers, this function will return a list with multiples of five removed

    >>> remove_multiples_of(5, [10,12,15,19])
    [12, 19]

    >>> remove_multiples_of(1, [1,2,3,4,5,6,7,8,9,10])
    []

    >>> remove_multiples_of(3, [5,10,15,20])
    [5, 10, 20]
    """
    out_put_list = []
    for number in numbers:
        if (float(number)%float(multiple)) != 0:
            out_put_list.append(number)
    return out_put_list


def solve_problem_1():
    max = 1000
    multiples_of_five = get_multiples_of(5, max)
    multiples_of_three = get_multiples_of(3, max)
    solution = 0
    for number in multiples_of_three:
        if number not in multiples_of_five:
            solution += number
    for number in multiples_of_five:
        solution += number
    return solution

print (solve_problem_1())
