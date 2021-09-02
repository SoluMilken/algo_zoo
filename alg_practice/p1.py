# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A.sort()
    print(A)
    min_value = min(A)
    max_value = max(A)
    n = len(A)

    if (min_value < 1) and (max_value < 1):
        return 1

    if max_value > 0:
        for i, a in enumerate(A):
            if a > 0:
                break

        min_pos_value = A[i]

        if min_pos_value != 1:
            return 1

        for j in range(i, n - 1):
            diff = A[j + 1] - A[j]
            print(j, diff)
            if diff > 1:
                return A[j] + 1
        return max_value + 1

        # for i in range(1, max_value + 1):
        #     if i not in A:
        #         return i
        # return max_value + 1


if __name__ == "__main__":
    print(solution([1, 3, 6, 4, 1, 2]))
