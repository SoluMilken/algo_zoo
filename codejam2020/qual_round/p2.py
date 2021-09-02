def p2(input_str):
    n = len(input_str)
    output_lst = ["" for _ in range(2 * n + 1)]

    if n == 1:
        output_lst[1] = input_str

    for i in range(n - 1):  # n > 1
        left = int(input_str[i])
        right = int(input_str[i + 1])

        output_lst[2 * i + 1] = str(left)
        output_lst[2 * i + 3] = str(right)

        if left == right:
            continue

        mid_ind = 2 * i + 2
        diff = abs(left - right)

        if left > right:
            output_lst[mid_ind] = ")" * diff
        else:
            output_lst[mid_ind] = "(" * diff

    # start
    output_lst[0] = "(" * int(input_str[0])
    # end
    output_lst[-1] = ")" * int(input_str[-1])

    return "".join(output_lst)


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        input_str = input()
        ans = p2(input_str)
        print("Case #{}: {}".format(i, ans))
