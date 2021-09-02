def p1(matrix):
    k = get_trace(matrix)
    r = get_number_of_repeated_rows(matrix)
    c = get_number_of_repeated_columns(matrix)
    return k, r, c


def get_trace(matrix):
    dim = len(matrix[0])
    trace = 0
    for i in range(dim):
        trace += matrix[i][i]
    return trace


def get_number_of_repeated_rows(matrix):
    dim = len(matrix[0])
    count = 0
    for i in range(dim):
        record = {}
        for j in range(dim):
            ele = matrix[i][j]
            if ele not in record:
                record[ele] = ele
            else:
                count += 1
                break
    return count


def get_number_of_repeated_columns(matrix):
    dim = len(matrix[0])
    count = 0
    for j in range(dim):
        record = {}
        for i in range(dim):
            ele = matrix[i][j]
            if ele not in record:
                record[ele] = ele
            else:
                count += 1
                break
    return count


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        matrix = []
        for _ in range(n):
            input_str = input()
            input_lst = input_str.split(" ")
            row = [int(ele) for ele in input_lst]
            matrix.append(row)
        k, r, c = p1(matrix)
        print("Case #{}: {} {} {}".format(i, k, r, c))
