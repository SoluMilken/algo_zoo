def solution(S):

    start_ind, a_count = get_a_stat(S)

    for count in a_count:
        if count > 2:
            return -1

    if len(start_ind) == 0:  # no a in S
        return (len(S) + 1) * 2
    # print(start_ind, a_count)

    result = 0
    # mid
    for i in range(1, len(start_ind)):
        start = start_ind[i - 1] + (a_count[i - 1] - 1)
        end = start_ind[i]
        result += (end - start - 2) * 2

        n_intv = end - start - 1

        if n_intv > 1:
            if a_count[i - 1] == 1:
                result += 1
                # a_count[i - 1] += 1
            if a_count[i] == 1:
                result += 1
                # a_count[i] += 1

    # start
    if start_ind[0] != 0:  # XXXXa
        result += start_ind * 2
        if a_count[0] == 1:  # XXXXaX
            result += 1

    if (start_ind[0] == 0) and (a_count[0] == 1):  # aXXXXXX
        result += 1

    # end
    if (start_ind[-1] + a_count[-1] - 1) != (len(S) - 1):
        end_ind = start_ind[-1] + a_count[-1] - 1
        S_end = len(S) - 1
        result += (S_end - end_ind) * 2

        if a_count[-1] == 1:
            result += 1

    return result


def get_a_stat(S):
    n = len(S)
    start_ind = []
    a_count = []
    count = 0

    for i in range(n):
        char = S[i]
        if char == "a":
            if count > 0:
                count += 1
            else:
                start_ind.append(i)
                count = 1
        else:
            if count > 0:
                a_count.append(count)

            count = 0

    if count > 0:
        a_count.append(count)

    return start_ind, a_count


if __name__ == "__main__":
    print(solution("abbabba"))
