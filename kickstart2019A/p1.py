
def p1(n, k, s):
    sorted_s = sorted(s)

    cum_sum = 0 
    target = sorted_s[k - 1]
    for i in range(k):
        cum_sum += (target - sorted_s[i])

    min_cum_sum = cum_sum
    for i in range(k, n):
        target = sorted_s[i]
        diff = target - sorted_s[i - 1]
        first_cost = sorted_s[i - 1] - sorted_s[i - k]
        current_cum_sum = cum_sum + diff * (k - 1) - first_cost
        
        # print(i, current_cum_sum)
        
        if current_cum_sum < min_cum_sum:
            min_cum_sum = current_cum_sum
        cum_sum = current_cum_sum

    return min_cum_sum


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = input().split(" ")
        s = input().split(" ")

        n = int(n)
        k = int(k)
        s = [int(ele) for ele in s]

        ans = p1(n, k, s)
        print("Case #{}: {}".format(i, ans))
