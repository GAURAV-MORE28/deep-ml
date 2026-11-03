import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    v = np.array(a)
    transpose = v.T

    return transpose

  