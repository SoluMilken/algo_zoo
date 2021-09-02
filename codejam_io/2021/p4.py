def get_score(
    left_idx: int,
    right_idx: int,
    B: str,
    odd: str,
    even: str,
    
    records: dict,
)
    # odd turn
    if left_idx == right_idx:
        # last pick
        if S[left_idx] == odd:
            records[(left_idx, right_idx)] = (1, -1)
        else:
            records[(left_idx, right_idx)] = (-1, 1)
        return records[(left_idx, right_idx)]

    if B[left_idx] == B[right_idx] and B[left_idx] == even:
        # odd has no choose
        records[(left_idx, right_idx)] = (-1, 1 + n)
        return records[(left_idx, right_idx)]

    left_odd_score, left_even_score = recur(
        left_idx + 1, right_idx, B, odd, even, records
    )
    right_odd_score, right_even_score = recur(
        left_idx, right_idx - 1, B, odd, even, records
    )

    if B[left_idx] == B[right_idx] and B[left_idx] == odd:
        # odd can choose leftmost and rightmost pieces
        if left_odd_score > right_odd_score:
            records[(left_idx, right_idx)] = (left_odd_score, left_even_score)
        else:
            records[(left_idx, right_idx)] = (right_odd_score, right_even_score)
        return records[(left_idx, right_idx)]

    elif B[left_idx] == odd:
        # odd can choose leftmost piece only
        records[(left_idx, right_idx)] = (left_odd_score, left_even_score)
        return records[(left_idx, right_idx)]

    else:
        # odd can choose rightmost piece only
        records[(left_idx, right_idx)] = (right_odd_score, right_even_score)
        return records[(left_idx, right_idx)]

def recur(
    left_idx: int,
    right_idx: int,
    B: str,
    odd: str,
    even: str,
    records: dict,
) -> int:
    n = right_idx - left_idx + 1
    if n % 2 == 1:
        # odd turn
        if left_idx == right_idx:
            # last pick
            if S[left_idx] == odd:
                records[(left_idx, right_idx)] = (1, -1)
            else:
                records[(left_idx, right_idx)] = (-1, 1)
            return records[(left_idx, right_idx)]

        if B[left_idx] == B[right_idx] and B[left_idx] == even:
            # odd has no choose
            records[(left_idx, right_idx)] = (-1, 1 + n)
            return records[(left_idx, right_idx)]

        left_odd_score, left_even_score = recur(
            left_idx + 1, right_idx, B, odd, even, records
        )
        right_odd_score, right_even_score = recur(
            left_idx, right_idx - 1, B, odd, even, records
        )

        if B[left_idx] == B[right_idx] and B[left_idx] == odd:
            # odd can choose leftmost and rightmost pieces
            if left_odd_score > right_odd_score:
                records[(left_idx, right_idx)] = (left_odd_score, left_even_score)
            else:
                records[(left_idx, right_idx)] = (right_odd_score, right_even_score)
            return records[(left_idx, right_idx)]

        elif B[left_idx] == odd:
            # odd can choose leftmost piece only
            records[(left_idx, right_idx)] = (left_odd_score, left_even_score)
            return records[(left_idx, right_idx)]

        else:
            # odd can choose rightmost piece only
            records[(left_idx, right_idx)] = (right_odd_score, right_even_score)
            return records[(left_idx, right_idx)]
    else:


def main(B: str) -> int:
    even = None
    odd = None
    if len(B) % 2 == 1:
        odd = "I"
        even = "O"
    else:
        odd = "O"
        even = "I"

    # acc_B = get_acc_B(B)

    # print(acc_B)

    # left_idx = 0
    # right_idx = len(B) - 1
    # for idx in range(len(B)):
    #     if idx % 2 == 0:
    #         result = i_round(B, left_idx, right_idx)
    #         if result is None:
    #             return "O", 1 + right_idx - left_idx + 1
    #         new_left_idx, new_right_idx = result
    #     else:
    #         result = o_round(B, left_idx, right_idx)
    #         if result is None:
    #             return "I", 1 + right_idx - left_idx + 1
    #         new_left_idx, new_right_idx = result
    #     left_idx, right_idx = new_left_idx, new_right_idx


if __name__ == "__main__":
    # T = int(input())
    # for case_i in range(1, T + 1):
    #     B = input()
    #     result = main(B)
    #     print("Case #{}: {}".format(case_i, result))

    print(main("IOIOOOII"))
    # N = 2
    # L = [5, 10]
    # print(main(N, L))
