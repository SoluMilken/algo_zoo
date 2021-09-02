from typing import List
import math


# def get_A(input_str, n_split):
#     input_len = len(input_str)
#     res = input_len % n_split
#     split_size = input_len // n_split
#     n_short_split = n_split - res
#     start_pos = 0
#     for split_i in range(n_split):
#         if split_i < n_short_split:
#             output_str = input_str[start_pos : start_pos + split_size]
#             start_pos += split_size
#         else:
#             output_str = input_str[start_pos : start_pos + split_size + 1]
#             start_pos += split_size + 1
#         if output_str[0] == '0':
#             output_str = '-1'
#         yield output_str


def is_valid_init(init_token: str, input_str: str):
    current_token = init_token
    current_int = int(current_token)

    start_pos = 0
    while True:
        target_token = input_str[start_pos : start_pos + len(current_token)]
        if target_token != current_token:
            return False
        start_pos += len(current_token)
        current_int += 1
        current_token = str(current_int)
    return True


def is_roaring_year(input_str: str):
    n = len(input_str)
    for init_len in range(2, n + 1):
        init_token = input_str[:init_len]
        if is_valid_init(init_token=init_token, input_str=input_str):
            return True
    return False

    # for n_split in range(2, n + 1):
    #     prev_str = None
    #     flag = True
    #     for out_str in get_A(input_str, n_split):
    #         if out_str == '-1':
    #             flag = False
    #             break
    #         if prev_str is None:
    #             prev_str = out_str
    #         else:
    #             if int(prev_str) + 1 != int(out_str):
    #                 flag = False
    #                 break
    #             else:
    #                 prev_str = out_str
    #     if flag:
    #         return True
    # return False


def main(Y: str):
    current_y_int = int(Y) + 1
    current_y = str(current_y_int)
    while True:
        if is_roaring_year(input_str=current_y):
            return current_y
        current_y_int += 1
        current_y = str(current_y_int)


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        Y = input()
        result = main(Y)
        print("Case #{}: {}".format(case_i, result))

    # # for result in get_A(input_str="9101112", n_split=4):
    # #     print(result)
    # print(is_roaring_year(input_str="2021"))
