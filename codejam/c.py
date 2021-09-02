def get_increasing_subseq_1(ants):
    # reverse normal ants order
    total_num = len(ants)
    output = []
    chosen = []
    for i, w in enumerate(ants):
        if i not in chosen:
            single_output = [w]
            for j in range(i+1, total_num):
                if ants[j] <= (6 * single_output[-1]):
                    single_output.append(ants[j])
                    chosen.append(j)
            output.append(single_output)
    return output


def get_increasing_subseq_2(ants):
    # reverse normal ants order
    total_num = len(ants)
    output = []
    chosen = []
    for i, w in enumerate(ants):
        if i not in chosen:
            single_output = [w]
            for j in range(i+1, total_num):
                if ants[j] <= single_output[-1]:
                    single_output.append(ants[j])
                    chosen.append(j)
            output.append(single_output)
    return output


def safe_or_not(ants):
    # reverse normal ants order
    total_weight = sum(ants)
    for w in ants:
        total_weight = total_weight - w
        if 6 * w < total_weight:
            return False
    return True


def main_p(ants):
    reversed_ants = ants[::-1]
    com_ants_1 = get_increasing_subseq_1(reversed_ants)
    com_ants_2 = get_increasing_subseq_2(reversed_ants)
    com_ants = com_ants_1
    com_ants.extend(com_ants_2)
    num_stack = 1
    for com_ant in com_ants:
        for j in range(len(com_ant) + 1)[::-1]:
            if len(com_ant[:j]) > num_stack:
                print(j)
                if safe_or_not(com_ant[:j]):
                    num_stack = len(com_ant[:j])
    return num_stack


if __name__ == '__main__':
    t = int(input()) # read a line with a single integer
    for i in range(1, t + 1):
        N = int(input())
        W = [int(s) for s in input().split(" ")]
        output = main_p(ants=W)
        print("Case #{}: {}".format(i, output))