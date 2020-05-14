# UFTM AI Course - Lesson 1 - Exercise 1

import numpy as np

epsilon = 0.8
N = 1000000
higher = 0
lower = 0

for i in range(N):
    r = np.random.rand()

    if r <= epsilon:
        lower += 1
    else:
        higher += 1

print(f'Percentage higher than epsilon: {(higher/N*100):.2f}%')
print(f'Percentage lower than epsilon: {(lower/N*100):.2f}%')
