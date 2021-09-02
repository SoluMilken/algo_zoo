def p3(n, d, slices):
    stats = {}
    for s in slices:
        if s not in stats:
            stats[s] = 1
        else:
            stats[s] += 1
    for degree, num in stats.items():
        if num >= d:
            return 0

    if d == 2:
        return 1

    if d == 3:
        for degree, num in stats.items():
            if num == 2:
                current_degree = degree
                for degree, num in stats.items():
                    if degree > current_degree:
                        return 1
            if degree * 2 in stats:
                return 1
        return 2


if __name__ == '__main__':

    t = int(input())
    for testcase_i in range(1, t + 1):
        n, d = input().split(" ")
        slices = input().split(" ")
        ans = p3(int(n), int(d), [int(s) for s in slices])
        print("Case #{}: {}".format(testcase_i, ans))
