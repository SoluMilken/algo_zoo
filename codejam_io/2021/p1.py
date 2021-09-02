from typing import List


def main(N: int, S: List[int]) -> int:
    weight2num = {}
    for s in S:
        if s not in weight2num:
            weight2num[s] = 1
        else:
            weight2num[s] += 1
    sorted_weight2num = sorted(weight2num.items(), key=lambda x: x[0])
    # print(sorted_weight2num)
    total_cost = 0
    for treat_cost, (weight, num) in enumerate(sorted_weight2num, start=1):
        total_cost += treat_cost * num
    return total_cost


if __name__ == "__main__":
    T = int(input())
    for case_i in range(1, T + 1):
        N = int(input())
        S = [int(ele) for ele in input().split(" ")]
        result = main(N, S)
        print("Case #{}: {}".format(case_i, result))
