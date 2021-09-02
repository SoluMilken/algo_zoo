import math


# def p3(n, q_ranges):
#     max_pos = n
#     for s, e in q_ranges:
#         n_pos = (e - s) + 1
#         if n_pos < max_pos:
#             max_pos = n_pos

#     for n_pos in range(max_pos, 0, -1):
#         output = recur(
#             visited_ranges=[], 
#             state=set(), 
#             q_ranges=q_ranges, 
#             target=n_pos,
#         )
#         if output:
#             return n_pos
#     return 0


def recur(visited_ranges, state, q_ranges, target):
    # print(visited_ranges, state, target)

    q = len(q_ranges)
    if len(visited_ranges) == q:
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

############

def is_overlapped(range1, range2):
    if (range1[0] > range2[1]) or (range1[1] < range2[0]):
        return False
    return True


def is_extended(range1, range2):
    if range1[1] == (range2[0] - 1):
        return True
    if range1[0] == (range2[1] + 1):
        return True
    return False


def get_overlapped_ranges(occupied_ranges, booking_range):
    overlapped_ranges = set()
    for i, occupied_range in enumerate(occupied_ranges):
        overlapped = is_overlapped(occupied_range, booking_range)
        if overlapped:
            overlapped_ranges.add(occupied_range)
    return overlapped_ranges


def get_extended_ranges(occupied_ranges, booking_range):
    extended_ranges = set()
    for i, occupied_range in enumerate(occupied_ranges):
        extended = is_extended(occupied_range, booking_range)
        if extended:
            extended_ranges.add(occupied_range)
    return extended_ranges


def merge_ranges(overlapped_ranges):
    output_start = 1e+9
    output_end = 0
    for overlapped_range in overlapped_ranges:
        output_start = min(overlapped_range[0], output_start)
        output_end = max(output_end, overlapped_range[1])
    return (output_start, output_end)


def get_avaliable_nseats(target_range, overlapped_ranges):
    n = target_range[1] - target_range[0] + 1

    for ds, de in overlapped_ranges:
        merged_start = max(ds, target_range[0])
        merged_end = min(de, target_range[1])
        diff = merged_end - merged_start + 1
        n -= diff
    return n


def run_one_step(occupied_ranges, booking_range):
    print(occupied_ranges, booking_range)

    overlapped_ranges = get_overlapped_ranges(occupied_ranges, booking_range)
    extended_ranges = get_extended_ranges(occupied_ranges, booking_range)
    # print(overlapped_ranges, extended_ranges)

    n_seats = get_avaliable_nseats(booking_range, overlapped_ranges)

    to_be_merge_ranges = overlapped_ranges.union(extended_ranges)

    if len(to_be_merge_ranges) > 0:
        to_be_merge_ranges.add(booking_range)
        merged_range = merge_ranges(to_be_merge_ranges)

        for to_be_merge_range in to_be_merge_ranges:
            if to_be_merge_range != booking_range:
                occupied_ranges.remove(to_be_merge_range) 
        occupied_ranges.add(merged_range)
    else:
        occupied_ranges.add(booking_range)
    print(n_seats)
    return occupied_ranges, n_seats


def p3(n, q_ranges):
    if len(set(q_ranges)) != len(q_ranges):
        return 0

    n_digits = int(math.log(n, 10))
    q = len(q_ranges)
    def key_function(x):
        overlapped_times = sum([is_overlapped(x, q_range) for q_range in q_ranges])
        q_len = x[1] - x[0] + 1
        value = (q - overlapped_times) * (10 ** (n_digits + 1))
        value += (q_len)
        return -value

    sorted_q_ranges = sorted(q_ranges, key=key_function)
    occupied_ranges = set()
    output = n

    for q_range in sorted_q_ranges:
        occupied_ranges, n_seats = run_one_step(occupied_ranges, q_range)
        output = min(n_seats, output)

    # layers = {}
    # occupied_ranges = set()
    # output = n

    # for q_range in q_ranges:
    #     ind =  q_range[1] - q_range[0]
    #     if ind not in layers:
    #         layers[ind] = set()
    #     layers[ind].add(q_range)

    # # print(layers)
    # sorted_layers = sorted(layers.items(), key=lambda x: x[0])

    # for layer_i in range(len(sorted_layers)):
    #     layer = sorted_layers[layer_i][1]
    #     if layer_i > 0:
    #         sorted_q_ranges = sorted(layer, key=lambda x: - sum(
    #             [int(is_overlapped(x, ele)) for ele in layer]))
    #     else:
    #         sorted_q_ranges = layer

    #     for q_range in sorted_q_ranges:
    #         occupied_ranges, n_seats = run_one_step(occupied_ranges, q_range)
    #         output = min(n_seats, output)
    return output


if __name__ == '__main__':
    # t = int(input())
    # for i in range(1, t + 1):
    #     n, q = input().split(" ")
    #     n = int(n)
    #     q = int(q)
    #     q_ranges = []
    #     for _ in range(q):
    #         s, e = input().split(" ")
    #         q_ranges.append((int(s), int(e)))

    #     ans = p3(n, q_ranges)
    #     print("Case #{}: {}".format(i, ans))

    q_ranges = [(33, 57),
                (126, 132),
                (22, 34),
                (13, 88),
                (106, 110),
                (105, 116),
                (107, 130),
                (101, 129),
                (85, 112)]
    # q_ranges = [(101, 129), (107, 130), (105, 116), (33, 57), (13, 88), (126, 132), (22, 34), (85, 112), (106, 110)]

    for q_range in q_ranges:
        value = sum([ int(is_overlapped(q_range, ele)) for ele in q_ranges])
        diff = q_range[1] - q_range[0] + 1
        print(q_range, diff, value)