def get_interest_level(matrix):
    score = 0
    for row in matrix:
        for ele in row:
            score += ele
    return score


def init_nbr_matrixs(r, c):

    def init_zero_matrix(r, c):
        matrix = []
        for _ in range(r):
            row = [0 for _ in range(c)]
            matrix.append(row)
        return matrix

    left = init_zero_matrix(r, c)
    right = init_zero_matrix(r, c)
    up = init_zero_matrix(r, c)
    down = init_zero_matrix(r, c)

    for i in range(r):
        for j in range(c):
            left[i][j] = j - 1
            up[i][j] = i - 1

            if (j + 1) < c:
                right[i][j] = j + 1
            else:
                right[i][j] = -1

            if (i + 1) < r:
                down[i][j] = i + 1
            else:
                down[i][j] = -1
    return left, right, up, down


def update_nbr_matrixs(i, j, left, right, up, down):
    # print(i, j, left, right, up, down)

    # left nbr
    if left[i][j] != -1:
        right[i][left[i][j]] = right[i][j]

    # right nbr
    if right[i][j] != -1:
        left[i][right[i][j]] = left[i][j]

    # up nbr
    if up[i][j] != -1:
        down[up[i][j]][j] = down[i][j]

    # down nbr
    if down[i][j] != -1:
        up[down[i][j]][j] = up[i][j]

    return left, right, up, down


def get_compass_nbrs(i, j, left, right, up, down):
    nbrs = []

    if left[i][j] != -1:
        nbrs.append((i, left[i][j]))

    if right[i][j] != -1:
        nbrs.append((i, right[i][j]))

    if up[i][j] != -1:
        nbrs.append((up[i][j], j))

    if down[i][j] != -1:
        nbrs.append((down[i][j], j))

    return nbrs


def get_avg_compass_score(nbrs, matrix):
    if len(nbrs) == 0:
        return 0.0

    score = 0
    for x, y in nbrs:
        score += matrix[x][y]
    return score / len(nbrs)


def compete(matrix, left, right, up, down):
    r = len(matrix)
    c = len(matrix[0])

    to_be_removed = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                continue

            nbrs = get_compass_nbrs(i, j, left, right, up, down)
            avg_score = get_avg_compass_score(nbrs, matrix)
            # print(i, j, nbrs, avg_score)

            if avg_score > matrix[i][j]:
                to_be_removed.append((i, j))

    # print(to_be_removed)
    # update matrix
    for x, y in to_be_removed:
        matrix[x][y] = 0
        left, right, up, down = update_nbr_matrixs(x, y, left, right, up, down)

    return matrix, left, right, up, down


def p3(r, c, matrix):
    left, right, up, down = init_nbr_matrixs(r, c)

    total_level = 0
    prev_level = 0
    while True:

        current_level = get_interest_level(matrix)
        if current_level == prev_level:
            break
        total_level += current_level

        matrix, left, right, up, down = compete(matrix, left, right, up, down)

        prev_level = current_level

    return total_level


# def p3(matrix):
#     org_matrix = matrix.copy()
#     r = len(matrix)
#     c = len(matrix[0])

#     r_dict = {}
#     c_dict = {}
#     for i in range(r):
#         for j in range(c):
#             if i not in r_dict:
#                 r_dict[i] = set({j})
#             else:
#                 r_dict[i].add(j)

#             if j not in c_dict:
#                 c_dict[j] = set({i})
#             else:
#                 c_dict[j].add(i)

#     score = 0
#     while True:
#         current_interest_level = get_interest_level(matrix)
#         matrix, r_dict, c_dict = eliminate_elements(matrix, r_dict, c_dict, org_matrix)
#         new_interest_level = get_interest_level(matrix)
#         score += current_interest_level
#         if new_interest_level == current_interest_level:
#             break
#     return score


# def eliminate_elements(matrix, r_dict, c_dict, org_matrix):
#     r = len(matrix)
#     c = len(matrix[0])
#     to_be_removed = []
#     for i, cols in r_dict.items():
#         for j in cols:
#             ac_score = avg_compass_score(i, j, r_dict, c_dict, org_matrix)
#             if ac_score > org_matrix[i][j]:
#                 to_be_removed.append((i, j))

#     for x, y in to_be_removed:
#         matrix[x][y] = 0
#         r_dict[x].remove(y)
#         c_dict[y].remove(x)

#     return matrix, r_dict, c_dict


# def avg_compass_score(i, j, r_dict, c_dict, matrix):
#     nbrs = get_compass_nbr(i, j, r_dict, c_dict)

#     if len(nbrs) == 0:
#         return 0

#     score = 0
#     count = 0
#     for x, y in nbrs:
#         score += matrix[x][y]
#         count += 1
#     # print(i, j, nbrs, score / count)
#     return score / count


# def get_compass_nbr(i, j, r_dict, c_dict):
#     output = []

#     cols = r_dict[i]
#     rows = c_dict[j]
#     # left
#     diff = [j - col for col in cols]

#     non_zero_diff = [ele for ele in diff if ele > 0]
#     if len(non_zero_diff) > 0:
#         output.append((i, j - min(non_zero_diff)))

#     # right
#     neg_diff = [abs(ele) for ele in diff if ele < 0]
#     if len(neg_diff) > 0:
#         output.append((i, j  + min(neg_diff)))

#     # up
#     diff = [i - row for row in rows]
#     non_zero_diff = [ele for ele in diff if ele > 0]
#     if len(non_zero_diff) > 0:
#         output.append((i - min(non_zero_diff), j))
#     # down
#     neg_diff = [abs(ele) for ele in diff if ele < 0]
#     if len(neg_diff) > 0:
#         output.append((i  + min(neg_diff), j))

#     return output




if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        r, c = input().split(" ")
        r = int(r)
        c = int(c)
        matrix = []
        for _ in range(r):
            input_lst = input().split(" ")
            row = [int(ele) for ele in input_lst]
            matrix.append(row)
        ans = p3(r, c, matrix)
        print("Case #{}: {}".format(i, ans))
