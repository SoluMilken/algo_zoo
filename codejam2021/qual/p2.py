def main(X, Y, S):
    # X: price of CJ
    # Y: price of JC
    q_idx_pairs = get_q_pos(S)
    # print(q_idx_pairs)
    s_lst = decide_q_chars(q_idx_pairs, S, X, Y)
    # print(s_lst)
    return get_cost(s_lst, X, Y)


def decide_q_chars(q_idx_pairs, S, X, Y):
    s_lst = [s for s in S]
    for start_idx, end_idx in q_idx_pairs:
        left_char = None
        right_char = None
        if start_idx > 0:
            left_char = S[start_idx - 1]
        if end_idx < len(S) - 1:
            right_char = S[end_idx + 1]

        if left_char is not None and right_char is not None:
            for idx in range(start_idx, end_idx + 1):
                s_lst[idx] = left_char
        elif left_char is None and right_char is not None:
            for idx in range(start_idx, end_idx + 1):
                s_lst[idx] = right_char
        elif left_char is not None and right_char is None:
            for idx in range(start_idx, end_idx + 1):
                s_lst[idx] = left_char
        else:
            for idx in range(start_idx, end_idx + 1):
                s_lst[idx] = "C"
    return s_lst


def get_q_pos(S):
    records = []
    prev_char = "X"
    S = S + "X"
    for idx, char in enumerate(S[:-1]):
        if prev_char != "?" and char == "?":
            start_idx = idx
        if char == "?" and S[idx + 1] != "?":
            end_idx = idx
            records.append((start_idx, end_idx))
        prev_char = char
    return records


def get_cost(s_lst, X, Y):
    cost = 0
    for idx in range(len(s_lst)):
        pattern = "".join(s_lst[idx : idx + 2])
        if pattern == "CJ":
            cost += X
        elif pattern == "JC":
            cost += Y
    return cost


if __name__ == "__main__":
    # # print(main(X=2, Y=3, S="CJ?CC?"))
    # print(main(X=2, Y=3, S="?"))
    # print(main(X=2, Y=3, S="J??C"))

    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        X_str, Y_str, S = input().split(" ")
        X, Y = int(X_str), int(Y_str)
        result = main(X, Y, S)
        print("Case #{}: {}".format(case_i, result))
