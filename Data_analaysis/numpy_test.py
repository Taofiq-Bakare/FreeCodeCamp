import numpy as np
from numpy.core.records import array
# from numpy.core.fromnumeric import mean


def convert(list):
    """
    Converts a list to numpy array
    """
    np_array = np.array(list, dtype=np.float16)
    return np_array


def to_mat(list):
    """
    Converts a numpy array to a matrix of shape 3*3
    """
    array = convert(list)
    mat_3 = np.reshape(array, (3, 3))
    return mat_3


def calc_mean(matrix):
    """
    A function to calculate the mean for the axis
    """
    all_mean = [np.mean(matrix, axis=0),
                np.mean(matrix, axis=1),
                np.mean(matrix)
                ]
    return all_mean


def calc_var(matrix):
    """
    A function to calculate the variance for the axis
    """
    all_var = [np.var(matrix, axis=0),
               np.var(matrix, axis=1),
               np.var(matrix)
               ]
    return all_var


def calc_std(matrix):
    """
    A function to calculate the std for the axis
    """
    all_std = [np.std(matrix, axis=0),
               np.std(matrix, axis=1),
               np.std(matrix)
               ]
    return all_std


def calc_max(matrix):
    """
    A function to calculate the max for the axis
    """
    all_max = [np.max(matrix, axis=0),
               np.max(matrix, axis=1),
               np.max(matrix)
               ]
    return all_max


def calc_min(matrix):
    """
    A function to calculate the min for the axis
    """
    all_min = [np.min(matrix, axis=0),
               np.min(matrix, axis=1),
               np.min(matrix)
               ]
    return all_min


def calc_sum(matrix):
    """
    A function to calculate the sum for the axis
    """
    all_sum = [np.sum(matrix, axis=0),
               np.sum(matrix, axis=1),
               np.sum(matrix)
               ]
    return all_sum


def calculate(list):
    """
    A function to collate the results into a dictionary
    """

    try:
        matrcs = to_mat(list)
        solutions = {'mean': calc_mean(matrcs),
                     'variance': calc_var(matrcs),
                     'standard deviation': calc_std(matrcs),
                     'max': calc_max(matrcs),
                     'min': calc_min(matrcs),
                     'sum': calc_sum(matrcs),
                     }
        return solutions
    except ValueError:
        print("The list is less 9")


number = [0, 1, 2, 3, 4, 5, 6, 7, 8]

solution_1 = calculate(number)

for key, value in solution_1.items():
    print(key, str(value))
