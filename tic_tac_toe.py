import numpy as np


def main():
    """Environment variables"""
    dim = 3
    dim2 = dim * dim

    vet_board = np.zeros(dim2)

    empty = 0
    o = 1
    x = -1
    N_episodes = 30000

    # initializing the Q-table
    Q = np.zeros((3**dim2, dim2))

    for episode in range(N_episodes):
        Q = play_one_episode(Q)
        # epsilon =
        # print()


def play_one_episode(Q, o, x, epsilon, dim2, vet_board, empty):
    game_over = False
    p1 = o
    p2 = x
    current_player = []
    recorded_state_action_reward = []
    state = get_state(dim2, vet_board, empty, o)

    while not game_over:
        # switch players
        current_player = p2 if current_player == p1 else p1

        # current_player makes a move
        if current_player == p1:
            action = take_action(epsilon, dim2, vet_board, empty) # apprentice robot
        else:
            action = take_action(1, dim2, vet_board, empty) # always random moves

        # filling the board
        vet_board[action] = current_player

        # checking if the match is over
        game_over, winner = game_over()

        # getting rewards
        reward = get_reward(game_over, winner, current_player)

        # changing to a new state
        new_state = get_state(dim2, vet_board, empty, o)

        # storage of the apprentice robot action-reward-state sequence
        if current_player == p1:
            recorded_state_action_reward.append((state, action, reward))

        # Q-table will be stored in a external for loop

        # atualizing state
        state = new_state

    for s_a_r in reversed(recorded_state_action_reward):
        Q[state, action] = (1 - alpha)*Q[state, action] + alpha*(reward + gamma*np.max(Q[new_state, :]))


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


def get_reward(game_over, winner, current_player):
    """1st get-reward strategy"""
    if game_over and winner == current_player:
        return 1
    else:
        return 0
