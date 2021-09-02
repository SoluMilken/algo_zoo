from collections import deque
import sys


def binary_search(result, x, left_idx, right_idx):
    if (left_idx + 1) == right_idx:
        print(left_idx, right_idx, file=sys.stderr)
        result.insert(right_idx, x)
        return result

    half_idx = (left_idx + right_idx) // 2
    print(
        "{} {} {}".format(result[half_idx], x, result[right_idx]),
        flush=True,
    )
    ans = int(input())
    print(
        "{} {} {} -> {}".format(result[half_idx], x, result[right_idx], ans),
        file=sys.stderr,
    )
    if ans == x:
        return binary_search(result, x, half_idx, right_idx)
    if ans == result[half_idx]:
        return binary_search(result, x, left_idx, half_idx)


def main(N):
    # first [1, 2, 3]
    result = deque()
    print("1 2 3", flush=True)
    ans = int(input())
    print(
        "1 2 3 -> {}".format(ans),
        file=sys.stderr,
    )
    if ans == 1:
        result.append(2)
        result.append(1)
        result.append(3)
    elif ans == 2:
        result.append(1)
        result.append(2)
        result.append(3)
    else:
        result.append(1)
        result.append(3)
        result.append(2)
    print(result, file=sys.stderr)
    for x in range(4, N + 1):
        print("{} {} {}".format(result[0], x, result[-1]), flush=True)
        ans = int(input())
        print(
            "{} {} {} -> {}".format(result[0], x, result[-1], ans),
            file=sys.stderr,
        )
        if ans == x:
            # inside
            result = binary_search(result, x, 0, len(result) - 1)
        elif ans == result[0]:
            result.appendleft(x)
        else:
            result.append(x)
        print(result, file=sys.stderr)

    print(" ".join([str(num) for num in result]), flush=True)
    correct_or_not = int(input())
    print(correct_or_not, file=sys.stderr)
    if correct_or_not == -1:
        sys.exit()


if __name__ == "__main__":
    T, N, Q = input().split(" ")
    T, N, Q = int(T), int(N), int(Q)

    for case_i in range(T):
        main(N)
