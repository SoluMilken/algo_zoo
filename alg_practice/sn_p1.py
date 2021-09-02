# def solution(N):
#     if N < 0:
#         sign = -1
#         str_N = str(N)[1:]
#     else:
#         sign = 1
#         str_N = str(N)

#     digits = [i for i in str_N]
#     n = len(digits)

#     candidates = []
#     for i in range(n + 1):
#         candidate = digits[0: i] + ["5"] + digits[i:]
#         candidates.append(candidate)

#     max_value = -100000
#     for cand in candidates:
#         int_cand = sign * int("".join(cand))
#         if int_cand > max_value:
#             max_value = int_cand

#     return max_value


def solution(N):
    if N < 0:
        sign = -1
        N = abs(N)
    else:
        sign = 1

    if N == 0:
        return 50

    max_value = -100000
    for i in range(5):
        quotient = N // (10 ** i)
        remainder = N % (10 ** i)
        # print(i, quotient, remainder, N)
        if remainder == N:
            break
        new_value = sign * ((quotient * (10 ** (i + 1))) + (5 * (10 ** i)) + remainder)
        # print(new_value)
        if new_value > max_value:
            max_value = new_value
    last_value = sign * (5 * (10 ** i) + N)
    return max(max_value, last_value)


if __name__ == "__main__":
    print(solution(700))
