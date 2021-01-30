import numpy as np

# from numpy.core.records import array
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
    all_mean = [(np.mean(matrix, axis=0).tolist()),
                (np.mean(matrix, axis=1).tolist()),
                np.mean(matrix).tolist()
                ]
    return all_mean


def calc_var(matrix):
    """
    A function to calculate the variance for the axis
    """
    all_var = [(np.var(matrix, axis=0).tolist()),
               (np.var(matrix, axis=1).tolist()),
               np.var(matrix).tolist()
               ]
    return all_var


def calc_std(matrix):
    """
    A function to calculate the std for the axis
    """
    all_std = [(np.std(matrix, axis=0).tolist()),
               (np.std(matrix, axis=1).tolist()),
               np.std(matrix).tolist()
               ]
    return all_std


def calc_max(matrix):
    """
    A function to calculate the max for the axis
    """
    all_max = [(np.max(matrix, axis=0).tolist()),
               (np.max(matrix, axis=1).tolist()),
               np.max(matrix).tolist()
               ]
    return all_max


def calc_min(matrix):
    """
    A function to calculate the min for the axis
    """
    all_min = [(np.min(matrix, axis=0).tolist()),
               (np.min(matrix, axis=1).tolist()),
               np.min(matrix).tolist()
               ]
    return all_min


def calc_sum(matrix):
    """
    A function to calculate the sum for the axis
    """
    all_sum = [(np.sum(matrix, axis=0).tolist()),
               (np.sum(matrix, axis=1).tolist()),
               np.sum(matrix).tolist()
               ]
    return all_sum


def calculate(list):
    """
      A function to collate the results into a dictionary
    """
    # if len(list) != 9:
    #   return "List must contain nine numbers."
    try:
        matrcs = to_mat(list)
        calculations = {'mean': calc_mean(matrcs),
                        'variance': calc_var(matrcs),
                        'standard deviation': calc_std(matrcs),
                        'max': calc_max(matrcs),
                        'min': calc_min(matrcs),
                        'sum': calc_sum(matrcs),
                        }
        return calculations
    except ValueError:
        return "List must contain nine numbers."


# number = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# solution_1 = calculate(number)
number = [2, 6, 2, 8, 4, 0, 1, 9]

solution_1 = calculate(number)

# for key, value in solution_1.items():
#     print(f"{key}, {value}")

# for key in solution_1:
#     print(f"{key};{solution_1[key]}")
print(solution_1)
