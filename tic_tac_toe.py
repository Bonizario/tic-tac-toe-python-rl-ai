import numpy as np

"""Environment variables"""
dim = 3
dim2 = dim * dim

vet_board = np.zeros(dim2)

empty = 0
o = 1
x = -1


def get_action(epsilon, dim2, vet_board, empty):
    """Returns the action to be taken by the agent"""
    r = np.random.rand()

    possible_actions = []
    for i in range(dim2):
        if vet_board(i) == empty:
            possible_actions.append(i)

    if r <= epsilon:
        n = len(possible_actions)
        index = np.random.choice(n)
        action = possible_actions[index]
        return action
    # else:
        # To do...
