import numpy as np


def calculate_mean_arr(matrix):
    return [
        list(np.mean(matrix, axis=0)),
        list(np.mean(matrix, axis=1)),
        np.mean(matrix),
    ]


def calculate_var_arr(matrix):
    return [
        list(np.var(matrix, axis=0)),
        list(np.var(matrix, axis=1)),
        np.var(matrix),
    ]


def calculate_std_dev_arr(matrix):
    return [
        list(np.std(matrix, axis=0)),
        list(np.std(matrix, axis=1)),
        np.std(matrix),
    ]


def calculate_max_arr(matrix):
    return [
        list(np.max(matrix, axis=0)),
        list(np.max(matrix, axis=1)),
        np.max(matrix),
    ]


def calculate_min_arr(matrix):
    return [
        list(np.min(matrix, axis=0)),
        list(np.min(matrix, axis=1)),
        np.min(matrix),
    ]


def calculate_sum_arr(matrix):
    return [
        list(np.sum(matrix, axis=0)),
        list(np.sum(matrix, axis=1)),
        np.sum(matrix),
    ]


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(list)
        mat_arr = arr.reshape(3, 3)

        mean_arr = calculate_mean_arr(mat_arr)
        var_arr = calculate_var_arr(mat_arr)
        std_dev_arr = calculate_std_dev_arr(mat_arr)
        max_arr = calculate_max_arr(mat_arr)
        min_arr = calculate_min_arr(mat_arr)
        sum_arr = calculate_sum_arr(mat_arr)

        calculation = {
            "mean": mean_arr,
            "variance": var_arr,
            "standard deviation": std_dev_arr,
            "max": max_arr,
            "min": min_arr,
            "sum": sum_arr,
        }
        return calculation


print("ans", calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))
