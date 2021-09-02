if __name__ == "__main__":
    T = int(input())
    for case_i in range(1, T + 1):
        N = int(input())
        As = [int(ele) for ele in input().split(" ")]
        result = main(N, As)
        print("Case #{}: {}".format(case_i, result))
