import math


def solution(predicted, observed):
    # write your code in Python 3.6
    n = len(predicted)
    square_error = 0
    for i in range(n):
        y_pred = predicted[i]
        y_true = observed[i]
        square_error += (y_pred - y_true) ** 2

    mean_square_error = square_error / n
    return math.sqrt(mean_square_error)


if __name__ == "__main__":
    print(solution([4, 25, 0.75, 11], [3, 21, -1.25, 13]))
