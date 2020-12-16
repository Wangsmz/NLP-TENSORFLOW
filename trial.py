import torch
print(torch.__version__)
import numpy as np
import math

x = [[x, y] for x in range(-10, 10) for y in range(-10, 10)]
y = list(map(lambda v: [1, 0, 0] if v[0] <= -math.sqrt(v[1] * v[1] + 1) else (
    [0, 0, 1] if v[0] >= math.sqrt(v[1] * v[1] + 1) else [0, 1, 0]), x))

print(np.array(x))
print(y)