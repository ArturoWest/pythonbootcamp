import pytest
from mathematica.algebra.matrices import add_matrices, sub_matrices

def add_matrices(): # matryca to jest lista list
    a = [
       [1,2,3],
       [4,5,6]
    ]

    b = [
       [7,8,9],
       [10,11,12]
    ]
    results = add_matrices(a,b)
    assert results == [
        [8,10,12],
        [14,16,18],
    ]

def test_add_matrices_with_diffrent_count_of_rows():
    a = [
        [1,2],
        [3,4],
        [5,6],
    ]

    b = [
        [7,8,9],
        [10,11,12],
    ]
    with pytest.raises(ValueError) as e:
        result = add_matrices(a, b)

def test_sub_matrices():
    a = [
       [1,2,3],
       [4,5,6]
    ]

    b = [
       [7,8,9],
       [10,11,12]
    ]
    results = add_matrices(a,b)
    assert results == [
        [-6,-6,-6],
        [-6,-6,-6],
    ]

def test_sub_matrices_with_diffrent_count_of_rows():
    a = [
        [1,2],
        [3,4],
        [5,6],
    ]

    b = [
        [7,8,9],
        [10,11,12],
    ]
    with pytest.raises(ValueError) as e:
        result = sub_matrices(a, b)