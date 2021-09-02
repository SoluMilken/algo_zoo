from typing import List


def fill_even_block(n: int):
    output = [chr(i) for i in range(65 + n - 1, 64, -1)]
    # print(output)
    return output


def fill_old_block(n: int, next_n: int):
    output = [chr(i) for i in range(66, 66 + n)]
    if ord(output[-1]) < (65 + next_n):
        output[-1] = chr(65 + next_n)
    return output


def main(N: int, L: List[int]) -> int:
    output = ["A"]
    for i in range(1, N + 1):
        if i % 2 == 1:
            if (i + 1) <= N:
                output.extend(fill_old_block(L[i - 1], L[i]))
            else:
                output.extend(fill_old_block(L[i - 1], 0))
        else:
            output.extend(fill_even_block(L[i - 1]))

    return "".join(output)


if __name__ == "__main__":
    T = int(input())
    for case_i in range(1, T + 1):
        N = int(input())
        L = [int(ele) for ele in input().split(" ")]
        result = main(N, L)
        print("Case #{}: {}".format(case_i, result))

    # N = 2
    # L = [5, 10]
    # print(main(N, L))
