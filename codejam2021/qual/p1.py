def reverse(num2idx, idx2num, i, j):
    half_idx = (j - i + 1) // 2
    for idx in range(half_idx):
        left_idx = i + idx
        right_idx = j - idx
        left_num = idx2num[left_idx]
        right_num = idx2num[right_idx]

        idx2num[left_idx] = right_num
        idx2num[right_idx] = left_num

        num2idx[right_num] = left_idx
        num2idx[left_num] = right_idx
    return num2idx, idx2num


def main(n, nums):
    num2idx = {num: i for i, num in enumerate(nums)}
    idx2num = {i: num for i, num in enumerate(nums)}
    cost = 0
    for i in range(n - 1):
        j = num2idx[i + 1]
        num2idx, idx2num = reverse(num2idx, idx2num, i, j)
        cost += j - i + 1
    return cost


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N = int(input())
        L = [int(num) for num in input().split(" ")]
        result = main(N, L)
        print("Case #{}: {}".format(case_i, result))
