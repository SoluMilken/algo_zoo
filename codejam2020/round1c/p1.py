def p1(x, y, steps):
    if (x, y) == (0, 0):
        return 0

    for i, step in enumerate(steps, start=1):
        if step == "N":
            y += 1
        elif step == "S":
            y -= 1
        elif step == "E":
            x += 1
        else:
            x -= 1
        dist = get_distance_from_O(x, y)
        if dist <= i:
            return i
    return "IMPOSSIBLE"


def get_distance_from_O(x, y):
    return abs(x) + abs(y)


if __name__ == '__main__':

    t = int(input())
    for testcase_i in range(1, t + 1):
        x, y, steps = input().split(" ")
        ans = p1(int(x), int(y), steps)
        print("Case #{}: {}".format(testcase_i, ans))
