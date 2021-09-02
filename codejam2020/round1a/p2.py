import math


def p2(n):
    if n == 1:
        return [(1, 1)]

    if n <= 1000:
        r = 1
        k = 1
        output_steps = [(1, 1)]
        visited = {(1, 1): 1}
        cum_score = 1

    else:
        r, k, output_steps, visited, cum_score = init2(n)

    print(r, k, output_steps, visited, cum_score)
    if cum_score == n:
        return output_steps

    output = recur(
        r=r,
        k=k,
        output_steps=output_steps,
        visited=visited,
        cum_score=cum_score,
        target=n,
    )
    return output


def init1(n):
    '''
    r
    k
    output_steps
    visited
    cum_score
    COMB
    '''

    # n ~ = 2^k - 1
    f = math.log(n + 1, 2)
    layer_floor = math.floor(f)
    layer_ceil = math.ceil(f)

    # get r, k
    if layer_floor == layer_ceil:
        r = layer_floor  # no need next step
        if layer_floor % 2 == 1:
            k = r
        else:
            k = 1
    else:
        r = layer_floor + 1  # need next step
        if r % 2 == 1:
            k = 1
        else:
            k = r

    output_steps = []
    visited = {}
    for i in range(1, layer_floor + 1):
        # print(i)
        if i % 2 == 1:
            columns = range(1, i + 1)
        else:
            columns = range(i, 0, -1)
        for j in columns:
            output_steps.append((i, j))
            visited[(i, j)] = 1
            get_score(i, j)

    # for next step
    if layer_floor != layer_ceil:
        output_steps.append((r, k))
        visited[(r, k)] = 1

    # cum score
    cum_score = 2**layer_floor - 1

    if layer_floor != layer_ceil:
        cum_score += 1

    # print(r, k, output_steps, visited, cum_score)
    return r, k, output_steps, visited, cum_score


def init2(n):
    '''
    r
    k
    output_steps
    visited
    cum_score
    '''
    half_n = int(n * (2/ 3))
    output_steps = []
    visited = {}
    for i in range(MAX_STEPS):
        if half_n > CUM_MAX_VALUE_IN_LAYER[i]:
            x = i + 1
            y = math.ceil((i+1) / 2)
            output_steps.append((x, y))
            visited[(x, y)] = 1
            cum_score = CUM_MAX_VALUE_IN_LAYER[i]
            r = x
            k = y
        else:
            break
    # print(r, k, output_steps, visited, cum_score)
    return r, k, output_steps, visited, cum_score


def recur(r, k, output_steps, visited, cum_score, target):
    # print(r, k, output_steps, cum_score)
    if len(output_steps) >= 500:
        print(output_steps)
        return

    next_steps = get_next_steps(r, k)

    for next_step in next_steps:
        if next_step not in visited:
            score = get_score(next_step[0], next_step[1])
            # print("outside, {} {} {}".format(next_step[0], next_step[1], score))
            current_cum_score = cum_score + score

            if current_cum_score == target:
                output_steps.append(next_step)
                return output_steps

            if current_cum_score <= target:
                output_steps.append(next_step)
                visited[next_step] = 1
                output = recur(
                    r=next_step[0],
                    k=next_step[1],
                    output_steps=output_steps,
                    visited=visited,
                    cum_score=current_cum_score,
                    target=target,
                )
                if output is not None:
                    return output

                output_steps.pop(-1)
                visited.pop(next_step)

    return


def get_next_steps(r, k):
    #  (ri - 1, ki - 1), (ri - 1, ki), (ri, ki - 1), (ri, ki + 1), (ri + 1, ki), (ri + 1, ki + 1).
    output_steps = set()
    for x, y in [(r - 1, k - 1), (r - 1, k), (r, k - 1),
                 (r, k + 1), (r + 1, k), (r + 1, k + 1)]:
        if (x > 0) and (y <= x) and (y > 0):
            output_steps.add((x, y))
    return output_steps


def get_score(row, kth):
    # print(row, kth, COMB[row][kth])

    row_ind = row - 1
    kth_ind = kth - 1

    # print(row, kth, COMB[row][kth])

    if COMB[row_ind][kth_ind] > 0:
        # print(row, kth, COMB[row_ind][kth_ind])
        return COMB[row_ind][kth_ind]

    if kth - 1 < 0:
        score = get_score(row - 1, kth)
    else:
        score = get_score(row - 1, kth - 1) + get_score(row - 1, kth)

    COMB[row_ind][kth_ind] = score
    # print(row, kth, score)
    # print(row, kth, COMB[row_ind][kth_ind])
    return score


def get_combination_number(n, k):
    # C(n, k)
    k = min(k, n - k)

    up = 1
    down = 1

    for v in range(n, n - k, -1):
        up *= v

    for v in range(1, k + 1):
        down *= v
    return up / down


if __name__ == '__main__':

    MAX_STEPS = 500

    MAX_VALUE_IN_LAYER = [0 for _ in range(MAX_STEPS)]
    CUM_MAX_VALUE_IN_LAYER = [0 for _ in range(MAX_STEPS)]

    for i in range(1, MAX_STEPS + 1):
        k = math.ceil(i / 2)
        MAX_VALUE_IN_LAYER[i - 1] = get_combination_number(i - 1, k - 1)
        CUM_MAX_VALUE_IN_LAYER[i - 1] = CUM_MAX_VALUE_IN_LAYER[i - 2] + MAX_VALUE_IN_LAYER[i - 1]
        COMB[i - 1][k - 1] = MAX_VALUE_IN_LAYER[i - 1]
        if CUM_MAX_VALUE_IN_LAYER[i - 1] > 1e+9:
            break

    COMB = []
    for i in range(MAX_STEPS):
        row = [0 for _ in range(i + 1)]
        row[0] = 1
        row[i] = 1
        COMB.append(row)

    FLAG = False

    t = int(input())
    for case_i in range(1, t + 1):
        n = int(input())
        steps = p2(n)
        print("Case #{}:".format(case_i))
        for step in steps:
            print("{} {}".format(step[0], step[1]))
