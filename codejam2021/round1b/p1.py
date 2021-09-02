from typing import List, Dict
from itertools import permutations
import math


def tick2nanosec(n_ticks: int, mode: str):
    if mode == "h":
        return n_ticks
    elif mode == "m":
        return n_ticks * (1 / 12)
    else:
        # s
        return n_ticks * (1 / 720)


def nanosec2hour(n_nanosec: int):
    return n_nanosec / (60 * 60 * 1e9)


def nanosec2min(n_nanosec: int):
    return n_nanosec / (60 * 1e9)


def nanosec2sec(n_nanosec: int):
    return n_nanosec / (1e9)


def gen_timestamp(A, B, C, modes):
    output = [0, 0, 0]
    for ticks, mode in zip([A, B, C], modes):
        nanosec = tick2nanosec(n_ticks=ticks, mode=mode)
        if mode == "h":
            result = nanosec2hour(nanosec)
            output[0] = result
        elif mode == "m":
            result = nanosec2min(nanosec)
            output[1] = result
        elif mode == "s":
            result = nanosec2sec(nanosec)
            output[2] = result
    return output


def is_int_nanosec(A, B, C, modes):
    for ticks, mode in zip([A, B, C], modes):
        nanosec = tick2nanosec(n_ticks=ticks, mode=mode)
        # print(nanosec, mode, ticks)
        if math.floor(nanosec) != nanosec:
            # print(nanosec, mode, ticks, False)
            return False
    # print(nanosec, mode, ticks, True)
    return True


def is_valid_timestamp(timestamp_list):
    h, m, s = timestamp_list
    if h < 0 or h >= 12:
        return False
    if m < 0 or m >= 60:
        return False
    if s < 0 and s >= 60:
        return False
    return True


def main(A, B, C):
    perm = permutations(["h", "m", "s"])
    for modes in list(perm):
        if not is_int_nanosec(A, B, C, modes):
            continue

        timestamp_list = gen_timestamp(A, B, C, modes)
        is_valid = is_valid_timestamp(timestamp_list)
        if is_valid:
            # print(modes)
            hh = int(timestamp_list[0])
            mm = int(timestamp_list[1])
            ss = int(timestamp_list[2])
            nano_sec = int((timestamp_list[2] - ss) * 1e9)
            print(f"{hh} {mm} {ss} {nano_sec}")
            # return f"{hh} {mm} {ss} {nano_sec}"


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        A, B, C = input().split(" ")
        A, B, C = int(A), int(B), int(C)
        result = main(A, B, C)
        print("Case #{}: {}".format(case_i, result))

    # A = 1476000000000
    # B = 2160000000000
    # C = 3723000000000

    # 3
    # 0 0 0
    # 0 21600000000000 23400000000000
    # 1476000000000 2160000000000 3723000000000

    # result = main(A, B, C)
    # print(A, B, C, result)
