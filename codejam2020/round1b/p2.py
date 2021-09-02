if __name__ == '__main__':

    t = int(input())
    for testcase_i in range(1, t + 1):
        n = int(input())
        patterns = []
        for _ in range(n):
            input_str = input()
            patterns.append(input_str)

        ans = p2(patterns)
        print("Case #{}: {}".format(testcase_i, ans))
