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

def get_state(dim2, vet_board, empty, o):
    """
    Converts the ternary representation of the board in a decimal number.
    Then, returns this decimal number, which represents the current state.

    E.g.: Given a 3x3 board, total_possibilities = 3*3*...*3 = 3^9 = 19682

    |0|1|2|    |8|7|6|5|4|3|2|1|0|
    |3|4|5| => ------------------- => 0*3^0 + 1*3^1 + 0*3^2 + ... + 1*3^8
    |6|7|8|    |1|2|1|0|0|2|0|1|0|
    """
    state = 0
    for i in range(dim2):
        if vet_board[i] == empty:
            digit = 0
        elif vet_board[i] == o:
            digit = 1
        else:
            digit = 2
        state = state + digit*3**i

    return state
