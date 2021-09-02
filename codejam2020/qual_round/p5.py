from typing import List


def gen_diag_recursively(
        diag: List[int],
        current_sum: int,
        ind: int,
        target: int,
    ):
    n = len(diag)
    if ind >= n:
        if current_sum == target:
            # print(ind, 'Y')
            return gen_matrix(diag)
        # print(ind, 'N')
        return

    diff = target - current_sum

    for value in range(1, min(n, diff) + 1):
        # print(ind, value)
        diag[ind] = value
        current_sum += value
        output = gen_diag_recursively(diag, current_sum, ind + 1, target)
        current_sum -= value
        if output is not None:
            return output


def gen_matrix(diag):
    n = len(diag)
    # init a matrix
    matrix = []
    for i in range(n):
        row = [-1 for _ in range(n)]
        row[i] = diag[i]
        matrix.append(row)

    output = gen_matrix_recursively(matrix, 0, 1)
    return output


def gen_matrix_recursively(matrix, i, j):
    # print(i, j, matrix)
    n = len(matrix[0])

    if i == j:
        if j == (n - 1):
            return matrix
        return gen_matrix_recursively(matrix, i, j + 1)

    candidates = get_valid_candidates(matrix, i, j)

    for cand in candidates:
        matrix[i][j] = cand
        if j == (n - 1):
            output = gen_matrix_recursively(matrix, i + 1, 0)
        else:
            output = gen_matrix_recursively(matrix, i, j + 1)

        if output is not None:
            return output

    matrix[i][j] = -1


def get_valid_candidates(matrix, i, j):
    # assert matrix[i][j] == -1
    n = len(matrix[0])

    existed_elements = set()
    for col_j in range(n):
        value = matrix[i][col_j]
        if value != -1:
            existed_elements.add(value)

    for row_i in range(n):
        value = matrix[row_i][j]
        if value != -1:
            existed_elements.add(value)

    return set(range(1, n + 1)) - existed_elements


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, k = input().split(" ")
        n = int(n)
        k = int(k)
        result = gen_diag_recursively(
            diag=[0 for _ in range(n)],
            current_sum=0,
            ind=0,
            target=k,
        )

        if result is None:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            print("Case #{}: POSSIBLE".format(i))
            for row in result:
                print(" ".join([str(ele) for ele in row]))

    # print(gen_matrix(diag=[1, 1, 3, 4]))
