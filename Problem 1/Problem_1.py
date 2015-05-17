__author__ = 'BatesG1996'

import Problem_1_helpers as p1
def solve_problem_1():
    max = 1000
    multiples_of_five = p1.get_multiples_of(5, max)
    multiples_of_three = p1.get_multiples_of(3, max)
    solution = 0
    for number in multiples_of_three:
        if number not in multiples_of_five:
            solution += number
    for number in multiples_of_five:
        solution += number
    return solution

print (solve_problem_1())