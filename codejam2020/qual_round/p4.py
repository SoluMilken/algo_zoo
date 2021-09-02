import sys
import random

MOD = 10


def reverse_str(s):
    new_s = s[::-1]
    return new_s

def flip_bit(s):
    output_lst = [str(1 - int(c)) for c in s]
    return ''.join(output_lst)


def b10():
    return query_bit(list(range(1, MOD + 1)))


def query_bit(indices):
    output_lst = []
    for i in indices:
        print(i, flush=True)
        digit = input()
        output_lst.append(digit)

    return "".join(output_lst)


def get_all_transformation(input_str):
    output_lst = []
    for i in range(4):
        if i == 1:
            tx_str = reverse_str(input_str)
        elif i == 2:
            tx_str = flip_bit(input_str)
        elif i == 3:
            tx_str = reverse_str(flip_bit(input_str))
        else:
            tx_str = input_str
        output_lst.append(tx_str)
    assert len(output_lst) == 4
    return output_lst


def match_str(tx_group_1, tx_group_2, target, indices):
    output1_str = None
    output2_str = None

    for tx1_str in tx_group_1:
        sub_tx1_lst = [tx1_str[ind - 1] for ind in indices]
        sub_tx1_str = "".join(sub_tx1_lst)
        if sub_tx1_str == target:
            output1_str = tx1_str
            break

    for tx2_str in tx_group_2:
        sub_tx2_lst = [tx2_str[ind - 1] for ind in indices]
        sub_tx2_str = "".join(sub_tx2_lst)
        if sub_tx2_str == target:
            output2_str = tx2_str
            break
    return output1_str, output2_str


def get_indices(tx_group_1, tx_group_2, b):

    total_set = tx_group_1.union(tx_group_2)
    # assert len(total_set) == len(tx_group_1) + len(tx_group_2)

    while True:
        indices = list(range(b))
        random.shuffle(indices)
        subindices = indices[:5]
        unique_set = set()

        for tx_str in total_set:
            sub_tx = [tx_str[ind] for ind in subindices]
            sub_tx = "".join(sub_tx)
            if sub_tx not in unique_set:
                unique_set.add(sub_tx)
            else:
                break
        if len(unique_set) == len(total_set):
            break
    return [ind + 1 for ind in subindices]


def b20():
    group1 = query_bit(list(range(1, MOD + 1)))
    group2 = query_bit(list(range(MOD + 1, 2 * MOD + 1)))

    tx_group_1 = set(get_all_transformation(group1))
    tx_group_2 = set(get_all_transformation(group2))

    for _ in range(9):
        if tx_group_1 == tx_group_2:
            group2 = query_bit(list(range(MOD + 1, 2 * MOD + 1)))
            tx_group_2 = set(get_all_transformation(group2))
        else:
            break
    # print(tx_group_1, tx_group_2, file=sys.stderr)


    indices = get_indices(tx_group_1, tx_group_2, MOD)
    # print(indices, file=sys.stderr)

    # print([ele[:: 2] for ele in tx_group_1], file=sys.stderr)
    # print([ele[:: 2] for ele in tx_group_2], file=sys.stderr)

    head = query_bit(indices)
    tail = query_bit([MOD + ind for ind in indices])

    # print("head: {} tail: {}".format(head, tail), file=sys.stderr)

    head1, head2 = match_str(tx_group_1, tx_group_2, head, indices)
    tail1, tail2 = match_str(tx_group_1, tx_group_2, tail, indices)

    # print(
    #     "head1: {} tail1: {} head2: {} tail2: {}".format(
    #         head1, tail1, head2, tail2), file=sys.stderr)

    if (head1 is not None) and (tail2 is not None):
        return head1 + tail2

    if (head2 is not None) and (tail1 is not None):
        return head2 + tail1


def p4(b):
    if b == 1 * MOD:
        output = b10()

    if b == 2 * MOD:
        output = b20()

    if output is not None:
        print(output, flush=True)
        response = input()
        if response == 'N':
            exit()
    return


if __name__ == '__main__':
    input_lst = input().split(" ")
    t = int(input_lst[0])
    b = int(input_lst[1])

    for i in range(t):
        # print(i, file=sys.stderr)
        p4(b)
