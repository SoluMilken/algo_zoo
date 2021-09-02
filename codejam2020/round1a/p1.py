import re

stars_pattern = re.compile(r"[*]+")


def p1(patterns):

    head_patterns = []  # XXX*
    tail_patterns = []  # *XXX
    mid_patterns = []  # *XXX*
    for pattern in patterns:
        pattern = stars_pattern.sub("*", pattern)
        head = pattern[0]
        tail = pattern[-1]
        pattern_list = pattern.split("*")
        start_ind = 0
        end_ind = len(pattern_list)
        if head != "*":
            head_patterns.append(pattern_list[0])
            start_ind = 1
        if tail != "*":
            tail_patterns.append(pattern_list[-1])
            end_ind -= 1
        mid_patterns.append("".join(pattern_list[start_ind: end_ind]))

    strict_head_pattern = gen_strict_pattern(head_patterns)
    strict_tail_pattern = gen_strict_pattern([p[::-1] for p in tail_patterns])[::-1]

    if (strict_head_pattern == "*") or (strict_tail_pattern == "*"):
        return "*"
    return strict_head_pattern + "".join(mid_patterns) + strict_tail_pattern



def gen_strict_pattern(patterns):
    '''
    patterns = [XXX, XXXX]
    '''
    if len(patterns) == 0:
        return ""

    sorted_patterns = sorted(patterns, key=lambda x: -len(x))
    n = len(sorted_patterns)

    most_strict_pattern = sorted_patterns[0]

    for i in range(1, n):
        current_pattern = sorted_patterns[i]
        s_len = len(current_pattern)
        for j in range(s_len):
            char = current_pattern[j]
            if char != most_strict_pattern[j]:
                if char != '*':
                    return '*'

    return most_strict_pattern


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        patterns = []
        for _ in range(n):
            input_str = input()
            patterns.append(input_str)

        ans = p1(patterns)
        print("Case #{}: {}".format(i, ans))
