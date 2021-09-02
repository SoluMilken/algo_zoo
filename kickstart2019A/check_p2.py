import random

from p2 import p2

def gen_test_case():
    r = random.randint(1, 10)
    c = random.randint(1, 10)

    matrix = []
    for _ in range(r):
        row = [str(random.randint(0, 1)) for _ in range(c)]
        matrix.append("".join(row))
    return r, c, matrix


if __name__ == '__main__':
    t = 10

    for _ in range(t):
        r, c, matrix = gen_test_case()
        print(r, c)
        for i in range(r):
            print(matrix[i])
        ans = p2(matrix, r, c)
        print(ans)
        print("------------")