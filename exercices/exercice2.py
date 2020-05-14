# UFTM AI Course - Lesson 1 - Exercise 2

import numpy as np

min_epsilon = 0.1
max_epsilon = 1
beta = 0.01 # change it to 0.1 and watch what happens
N = 1000
higher = 0
lower = 0

for i in range(N):
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-beta*i)

    r = np.random.rand()

    if r <= epsilon:
        lower += 1
    else:
        higher += 1

print(f'Percentage higher than epsilon: {(higher/N*100):.2f}%')
print(f'Percentage lower than epsilon: {(lower/N*100):.2f}%')
