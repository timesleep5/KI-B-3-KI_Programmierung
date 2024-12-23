from z3 import sat, Solver, Optimize


def unique_solution(solver, variables):
    """
    Determines if the current model has one unique solution.
    :param solver: The solver.
    :param variables: The variables occurring in the model.
    :return: True if the model has exactly one unique solution, False otherwise.
    """
    model = solver.model()
    for variable in variables:
        solver.push()
        # model completion: z3 would return the variable itself if it does not influence the outcome of the formula, but model_completion=True fills such variables with arbitrary values
        solver.add(variable != model.eval(variable,
                                          model_completion=True))
        if solver.check() == sat:
            print(solver.model())
            solver.pop()
            return False
        solver.pop()
    return True


def print_if_solvable(solver: Solver | Optimize):
    check = solver.check()
    print(check)
    if check == sat:
        print(solver.model())
