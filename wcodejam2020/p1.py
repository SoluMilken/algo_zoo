from collections import deque


def p1(input_str):
    # IO
    nI = 0
    ni = 0
    count = 0
    for char in input_str:
        if char == 'I':
            nI += 1
        
        if char == 'i':
            ni += 1
        
        if char == 'O':
            if nI > 0:
                nI -= 1
                count += 1
            elif ni > 0:
                ni -= 1

        if char == 'o':
            if ni > 0:
                ni -= 1
            elif nI > 0:
                nI -= 1

    return count

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        input_str = input()
        ans = p1(input_str)
        print("Case # {}: {}".format(i, ans))
