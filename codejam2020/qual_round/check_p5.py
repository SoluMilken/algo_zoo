import random

from p1 import (
    get_number_of_repeated_columns,
    get_number_of_repeated_rows,
    get_trace,
)
from p5 import gen_diag_recursively


def gen_latin_matrix(n):
    output_list = []
    for i in range(n):
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        output_list.append(numbers)

    return output_list


def check_natual_latin_matrix(matrix):
    count = get_number_of_repeated_columns(matrix)
    if count > 0:
        return False
    return True

def main(n):
    result = set()
    for _ in range(1000000):
        matrix = gen_latin_matrix(n)
        # print(matrix)
        if check_natual_latin_matrix(matrix):
            trace = get_trace(matrix)
            result.add(trace)

        if result == (n*n - n + 1):
            break
    print(result)
    return result




if __name__ == '__main__':
    main(50)
    #3:  {3, 6, 9}
    #4:  {4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16}
    #5:  {13, 15, 18, 19, 20, 25}

    # n = 5
    # for k in {13, 15, 18, 19, 20, 25}:
    #     print(k)
    #     output = gen_diag_recursively(
    #         diag=[0 for _ in range(n)],
    #         current_sum=0,
    #         ind=0,
    #         target=k,
    #     )
    #     print(output)
