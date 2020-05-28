import numpy as np


def main():
    """Environment variables"""
    dim = 3
    dim2 = dim * dim

    # vet_board = np.zeros(dim2)

    empty = 0
    o = 1
    x = -1
    N_episodes = 30000

    # initializing the Q-table
    Q = np.zeros((3**dim2, dim2))

    # episodes parameters
    N_episodes = 30000
    alpha = 0.5  # learning rate
    gamma = 0.95  # discount rate
    min_epsilon = 0  # 0% probability to take random actions
    max_epsilon = 1  # 100% probability to take random actions
    decay_rate = 0.001  # if too high, epsilon will approach 0 too fast
    epsilon = 1

    for episode in range(N_episodes):
        Q = play_one_episode(Q, o, x, epsilon, dim2, empty, alpha, gamma)
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * \
            np.exp(-decay_rate * episode)
        if episode % 1000 == 0:
            print(epsilon)

    # play_teste()


def play_teste(Q, dim2, empty, x, o):
    vet_board = np.zeros(dim2)
    game_over = False
    p1 = o
    p2 = x
    current_player = []
    state = get_state(dim2, vet_board, empty, o)

    while not game_over:
        # switch players
        current_player = p2 if current_player == p1 else p1

        # current_player makes a move
        if current_player == p1:
            # robot uses only his experiences (epsilon == 0)
            action = get_action(Q, state, 0, dim2, vet_board, empty)
        else:
            action = int(input('Faça sua jogada: '))

        # filling the board
        vet_board[action] = current_player

        # checking if the match is over
        game_over, winner = game_over()

        # changing to a new state
        new_state = get_state(dim2, vet_board, empty, o)

        # atualizing state, Q-table will be stored in a external for loop
        state = new_state


def play_one_episode(Q, o, x, epsilon, dim2, empty, alpha, gamma):
    vet_board = np.zeros(dim2)
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
            # apprentice robot
            action = get_action(Q, state, epsilon, dim2, vet_board, empty)
        else:
            # always random moves
            action = get_action(Q, state, 1, dim2, vet_board, empty)

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

        # atualizing state, Q-table will be stored in a external for loop
        state = new_state


def get_action(Q, state, epsilon, dim2, vet_board, empty):
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
    else:
        Q_vals = Q[state, :]
        Q_possible = [Q_vals[i] for i in possible_actions]
        max_Q_possible = np.max(Q_possible)  # not random for 2 or more max
        actions_max = [i for i in possible_actions if Q_vals == max_Q_possible]
        action = np.random.choice(actions_max)


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


def game_over(vet_board, dim, x, o):
    mat_board = np.reshape(vet_board, (dim, dim))

    for player in (x, o):
        for i in range(dim):
            if mat_board[i, :].sum() == player*dim:  # check lines
                winner = player
                return True, winner
            elif mat_board[:, i].sum() == player*dim:  # check columns
                winner = player
                return True, winner

    # check diagonals
    for player in (x, o):
        if np.sum(np.diag(mat_board)) == player*dim:  # primary
            winner = player
            return True, winner
        elif np.sum(np.diag(np.fliplr(mat_board))) == player*dim:  # secondary
            winner = player
            return True, winner

    if np.all((mat_board == 0) is False):  # all fields are not empty
        winner = None
        return True, winner

    # game in not over yet
    winner = None
    return False, winner


def draw_board(vet_board, x, o, dim):
    mat_board = np.resize(vet_board, (dim, dim))

    print(' ', end='')
    print('  1', end='  ')
    print(' 2', end='  ')
    print(' 3', end='  ')
    print('')
    print('-------------')

    for i in range(dim):
        print(str(i + 1), end=' ')
        for j in range(dim):
            print(' ', end='')
            if mat_board[i, j] == x:
                print('X  ', end='')
            elif mat_board[i, j] == o:
                print('O  ', end='')
            else:
                print('-  ', end='')
        print('')
