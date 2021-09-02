import random

from p3 import p3



def merge_timeinv(input_lst):
    sorted_lst = sorted(input_lst, key = lambda s: s[0] * 10000 + s[1])

    while True:
        n = len(sorted_lst)
        for i in range(n - 1):
            left = sorted_lst[i]
            right = sorted_lst[i + 1]
            if right[0] >= left[1]:
                continue
            else:
                new_time_inv = (min(left[0], right[0]), max(left[1], right[1]))
                sorted_lst = sorted_lst[0: i] + [new_time_inv] + sorted_lst[i+2:]
                break
        m = len(sorted_lst)
        if n == m:
            break
    return sorted_lst


def check_overlap(input_lst):
    disjoint_time_inv = merge_timeinv(input_lst)
    # print(disjoint_time_inv)
    # print(input_lst)
    count = [0 for _ in disjoint_time_inv]

    for time_inv in input_lst:
        start_time, end_time = time_inv
        dtv = len(disjoint_time_inv)
        for i in range(dtv):
            d_time_inv = disjoint_time_inv[i]
            d_start_time, d_end_time = d_time_inv
            if (start_time >= d_start_time) and (end_time <= d_end_time):
                count[i] += 1

    # import pdb; pdb.set_trace()
    # print(count)
    # print(disjoint_time_inv)
    if sum(count) != len(input_lst):
        print(count)
        print(input_lst)
        print(disjoint_time_inv)
        assert count == len(input_lst)
    return count


def check_p3(input_lst, result):

    if result == "IMPOSSIBLE":
        # check overlap more than 2 times
        count = check_overlap(input_lst)
        assert max(count) > 2

    else:
        if len(result) != len(input_lst):
            print(result)
            print(input_lst)
            assert len(result) == len(input_lst)

        C = []
        J = []
        for i, char in enumerate(result):
            if char == "C":
                C.append(input_lst[i])
            else:
                J.append(input_lst[i])

        # print(C, J)
        merged_C = merge_timeinv(C)
        if len(merged_C) != len(C):
            print(input_lst)
            print(C)
            print(merged_C)
            assert len(merged_C) == len(C)

        merged_J = merge_timeinv(J)
        if len(merged_J) != len(J):
            print(input_lst)
            print(J)
            print(merged_J)
            assert len(merged_J) == len(J)

        # count_C = check_overlap(C)
        # count_J = check_overlap(J)

        # # print(count_C, count_J)
        # for ele in count_C:
        #     assert ele == 1
        # for ele in count_J:
        #     assert ele == 1


if __name__ == '__main__':
    T = 1000
    N = random.randint(2, 1000)
    for t in range(T):
        # print(t)
        input_lst = []
        for n in range(N):
            start_time = random.randint(0, 24 * 60 - 1)
            end_start_time = start_time + 1
            end_time = random.randint(end_start_time, 24 * 60)
            input_lst.append((start_time, end_time))
        # print(input_lst)
        result = p3(input_lst)
        # print(result)
        check_p3(input_lst, result)
