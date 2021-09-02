# Qualification Round
# Reversort Engineering (7pts, 11pts)


def reverse(input_list, target_idx):
    half_idx = target_idx // 2
    for idx in range(half_idx + 1):
        input_list[idx], input_list[target_idx - idx] = (
            input_list[target_idx - idx],
            input_list[idx],
        )
    return input_list


def recur(step_i: int, cost: int, records: dict, N: int):
    if (step_i, cost) in records:
        return records[(step_i, cost)]
    if step_i == N - 2:
        # last step
        if cost == 1:
            records[(step_i, cost)] = [N - 1, N]
        elif cost == 2:
            records[(step_i, cost)] = [N, N - 1]
        else:
            records[(step_i, cost)] = -1
        return records[(step_i, cost)]

    if cost < 1:
        records[(step_i, cost)] = -1
        return records[(step_i, cost)]

    valid_cost = min(cost, N - step_i)
    for current_cost in range(1, valid_cost + 1):
        result = recur(step_i + 1, cost - current_cost, records, N)
        # print(step_i, current_cost, result)
        if result != -1:
            output = [step_i + 1] + result
            # print(output, cost)
            output = reverse(output, current_cost - 1)
            records[(step_i, cost)] = output
            return records[(step_i, cost)]
    records[(step_i, cost)] = -1
    return -1


def main(N, C):
    records = {}
    result = recur(step_i=0, cost=C, records=records, N=N)
    # print(records)
    if result == -1:
        return "IMPOSSIBLE"
    result_str = [str(ele) for ele in result]
    return " ".join(result_str)


def get_index(input_list, target_val):
    for idx in range(len(input_list)):
        if input_list[idx] == target_val:
            return idx
    # print(input_list, target_val)


def reverse_mid(input_list, left_idx, right_idx):
    # print(input_list, left_idx, right_idx)
    half_idx = (right_idx - left_idx) // 2
    for idx in range(half_idx + 1):
        input_list[idx + left_idx], input_list[right_idx - idx] = (
            input_list[right_idx - idx],
            input_list[idx + left_idx],
        )
    return input_list


def check(input_list):
    n = len(input_list)
    cost = 0
    for ele in range(1, n):
        idx = get_index(input_list, ele)
        cost += idx - (ele - 1) + 1
        # print(ele, idx, cost, input_list)
        input_list = reverse_mid(input_list=input_list, left_idx=ele - 1, right_idx=idx)
        # print(input_list)
    return cost


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N, C = input().split(" ")
        N, C = int(N), int(C)
        result = main(N, C)
        print("Case #{}: {}".format(case_i, result))

    # import random
    # for _ in range(100):
    #     C = random.randint(1, 1000)
    #     N = random.randint(2, 100)
    #     result = main(N, C)
    #     if result != "IMPOSSIBLE":
    #         int_list = [int(ele) for ele in result.split(" ")]
    #         expected_result = check(int_list)
    #         if expected_result != C:
    #             print(f"N={N}, C={C}, result={result}, realC={expected_result}")
    #     else:
    #         print(f"N={N}, C={C}, result={result}")

    # import random
    # for _ in range(1000):
    #     # C = random.randint(1, 1000)
    #     N = random.randint(2, 100)
    #     input_list = [ele for ele in range(1, N + 1)]
    #     random.shuffle(input_list)
    #     C = check(input_list.copy())
    #     result = main(N, C)
    #     if result == "IMPOSSIBLE":
    #         print(f"IMPOSSIBLE, N={N}, C={C}, ans={input_list}")
    #     else:
    #         int_list = [int(ele) for ele in result.split(" ")]
    #         expected_result = check(int_list)
    #         if expected_result != C:
    #             print(f"N={N}, C={C}, result={result}, realC={expected_result}")

    # result = "1 2 3 4 5"
    # int_list = [int(ele) for ele in result.split(" ")]
    # expected_result = check(int_list)
    # print(int_list, expected_result)

    # result = main(N=4, C=8)
    # print(result)
