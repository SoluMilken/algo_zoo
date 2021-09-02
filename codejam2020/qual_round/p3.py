def p3(input_lst):
    n = len(input_lst)

    idx_map = {}
    for i in range(n):
        if input_lst[i] not in idx_map:
            idx_map[input_lst[i]] = [i]
        else:
            idx_map[input_lst[i]].append(i)

    output_lst = ["" for _ in range(n)]
    sorted_lst = sorted(input_lst, key = lambda s: s[0] * 10000 + s[1])

    C = sorted_lst[0][1]
    J = 0
    ind = idx_map[sorted_lst[0]][0]
    output_lst[ind] = "C"

    if len(idx_map[sorted_lst[0]]) > 1:
        idx_map[sorted_lst[0]].pop(0)


    for i in range(1, n):
        start_time, end_time = sorted_lst[i]
        if start_time < C:
            if start_time >= J:
                J = end_time
                ind = idx_map[sorted_lst[i]][0]
                output_lst[ind] = "J"
            else:
                return "IMPOSSIBLE"
        else:
            C = end_time
            ind = idx_map[sorted_lst[i]][0]
            output_lst[ind] = "C"

        if len(idx_map[sorted_lst[i]]) > 1:
            idx_map[sorted_lst[i]].pop(0)

    return "".join(output_lst)


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        time_lst = []
        for _ in range(n):
            input_str = input()
            input_lst = input_str.split(" ")
            time_inv = (int(input_lst[0]), int(input_lst[1]))
            time_lst.append(time_inv)
        ans = p3(time_lst)
        print("Case #{}: {}".format(i, ans))
