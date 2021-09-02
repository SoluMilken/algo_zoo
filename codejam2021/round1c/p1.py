from typing import List


# def get_maxlen_interval(empty_interval):
#     maxlen = 0
#     for intv in empty_interval:
#         start_pos, end_pos = intv
#         intv_len = end_pos - start_pos + 1
#         maxlen = max(intv_len, maxlen)
#     return maxlen


def get_next_maxlen(intv_lens, target_val):
    for i, val in enumerate(intv_lens):
        if val == target_val:
            break
    return max(intv_lens[0:i] + intv_lens[i + 1 :])


def main(N: int, K: int, Ps: List[int]):
    Ps = set(Ps)
    sorted_Ps = sorted(Ps)

    intv_lens = []
    for i in range(len(sorted_Ps) - 1):
        current_p = sorted_Ps[i]
        next_p = sorted_Ps[i + 1]
        if current_p + 1 == next_p:
            continue
        intv_len = (next_p - 1) - (current_p + 1) + 1
        intv_lens.append(intv_len)

    left_len = 0
    right_len = 0

    if sorted_Ps[0] != 1:
        left_len = sorted_Ps[0] - 1
    if sorted_Ps[-1] != K:
        right_len = K - (sorted_Ps[-1] + 1) + 1

    if len(intv_lens) == 0:
        return (left_len + right_len) / K

    mid_maxlen = max(intv_lens)
    if mid_maxlen % 2 == 0:
        half_score = mid_maxlen // 2
    else:
        half_score = (mid_maxlen // 2) + 1

    if len(intv_lens) == 1:
        return max(
            [
                mid_maxlen,
                half_score + left_len,
                half_score + right_len,
                left_len + right_len,
            ]
        ) / K
    mid_next_maxlen = get_next_maxlen(intv_lens, mid_maxlen)
    if mid_next_maxlen % 2 == 0:
        next_half_score = mid_next_maxlen // 2
    else:
        next_half_score = (mid_next_maxlen // 2) + 1

    return max(
        [
            mid_maxlen,
            half_score + next_half_score,
            half_score + left_len,
            half_score + right_len,
            left_len + right_len,
        ]
    ) / K




if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N, K = input().split(" ")
        N, K = int(N), int(K)
        Ps = input().split(" ")
        Ps = [int(p) for p in Ps]
        result = main(N, K, Ps)
        print("Case #{}: {}".format(case_i, result))
    # N = 4
    # K = 7
    # Ps = [1, 3, 5, 7]
    # result = main(N, K, Ps)
    # print(result)
