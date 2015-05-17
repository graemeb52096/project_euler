__author__ = 'BatesG1996'

import Problem_2_helpers as p2
def solve_problem_2():
    max = 4000000
    fib = p2.get_fibonacci(max)
    fib_evens = p2.remove_odds_from_list(fib)
    return sum(fib_evens)

print (solve_problem_2())
