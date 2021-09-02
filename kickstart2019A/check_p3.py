def p3(n, q_ranges):
    max_pos = n
    for s, e in q_ranges:
        n_pos = (e - s) + 1
        if n_pos < max_pos:
            max_pos = n_pos

    for n_pos in range(max_pos, 0, -1):
        output = recur(
            visited_ranges=[], 
            state=set(), 
            q_ranges=q_ranges, 
            target=n_pos,
        )
        if output:
            return n_pos
    return 0


def recur(visited_ranges, state, q_ranges, target):
    # print(visited_ranges, state, target)

    q = len(q_ranges)
    if len(visited_ranges) == q:
        print(visited_ranges)
        for ind in visited_ranges:
            print(q_ranges[ind])
        return True
    
    next_steps = get_avaliable_candidates(visited_ranges, q)

    for step in next_steps:
        s, e = q_ranges[step]
        expected_pos = set(range(s, e + 1))
        union_state = state | expected_pos
        diff = len(union_state) - len(state)
        
        if diff < target:
            continue
        
        visited_ranges.append(step)
        output = recur(
            visited_ranges=visited_ranges, 
            state=union_state, 
            q_ranges=q_ranges, 
            target=target,
        )
        visited_ranges.pop(-1)
        if output:
            return True

    return False


def get_avaliable_candidates(visited_ranges, q):
    return set(range(0, q)) - set(visited_ranges)


if __name__ == '__main__':
    '''
        Time limit: 30 seconds per test set.
        Memory limit: 1GB.
        T = 100.
        1 ≤ N ≤ 106.
        1 ≤ Li ≤ Ri ≤ N.
        Test set 1 (Visible)

        1 ≤ Q ≤ 300.
        Test set 2 (Hidden)

        1 ≤ Q ≤ 30000.
        For at least 85 of the test cases, Q ≤ 3000. 
    '''

    import random
    from p3 import p3 as current_p3

    # MAX_N = 1000
    # for t in range(10):
    #     n = random.randint(1, MAX_N)
    #     q = random.randint(1, 10)
    #     print(t, n, q)

    #     q_ranges = []
    #     for _ in range(q):
    #         l = random.randint(1, n)
    #         r = random.randint(l, n)
    #         q_ranges.append((l, r))

    #     bf_result = p3(n, q_ranges)
    #     current_result = current_p3(n, q_ranges)
    #     if bf_result != current_result:
    #         print(n, q)
    #         print(q_ranges)
    #         print(bf_result)
    #         print(current_result)
    current_p3(
        134, 
        [(101, 129), (107, 130), (105, 116), (33, 57), (13, 88), (126, 132), (22, 34), (85, 112), (106, 110)]
    )


'''
134 9
[(101, 129), (107, 130), (105, 116), (33, 57), (13, 88), (126, 132), (22, 34), (85, 112), (106, 110)]
4
0

(33, 57)
(126, 132)
(22, 34)
(13, 88)
(106, 110)
(105, 116)
(107, 130)
(101, 129)
(85, 112)
'''