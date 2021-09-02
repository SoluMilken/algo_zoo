def solution(A):
    # write your code in Python 3.6
    n = len(A)
    i = 0
    while i < n:
        val = A[i]
        if val < 1:
            del A[i]
            n -= 1
        else:
            i += 1
    if len(A) == 0:
        return 1
    A = set(A)
    A = sorted(A)
    min_val = min(A)

    if min_val > 1:
        return 1

    max_val = max(A)
    pt = 1
    for val in range(min_val + 1, max_val):
        if val != A[pt]:
            return val
        pt += 1
    return max_val + 1


if __name__ == "__main__":
    A = [1, 3, 6, 4, 1, 2]
    A = [2]
    print(solution(A))
