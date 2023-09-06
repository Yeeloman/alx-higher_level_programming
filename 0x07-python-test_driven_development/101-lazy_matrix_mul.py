#!/usr/bin/python3

"""

Module composed by a function that multiplies 2 matrices

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul.

    Args:
        m_a: matrix a.
        m_b: matrix b.
    """
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("Matrix shapes are not compatible for multiplication")
