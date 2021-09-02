import math

def p1(x, y):
    if (abs(x) % 2) == (abs(y) % 2):
        return "IMPOSSIBLE"

    # if (abs(x) <= 4) and (abs(y) <= 4):
    max_step = int(math.log(max(abs(x), abs(y)), 2)) + 1
    # print(max_step)
    # import ipdb; ipdb.set_trace()
    output = recur(1, (0, 0), (x, y), [], max_step)
    if output is None:
        return "IMPOSSIBLE"
    return "".join(output)


def recur(step_size, curr_pos, target, output_steps, max_iter):
    # print(step_size, output_steps, curr_pos, target)
    if (curr_pos[0] == target[0]) and (curr_pos[1] == target[1]):
        final_steps = output_steps.copy()
        # print(final_steps)
        return final_steps

    if step_size > (2 ** max_iter):
        return

    x, y = target

    if x % 2 == 1:
        odd_pos = x
        even_pos = y
    else:
        odd_pos = y
        even_pos = x

    if step_size == 1:
        if x % 2 == 1:
            output_steps.append("E")
            output1 = recur(step_size * 2, (curr_pos[0] + 1, curr_pos[1]), target, output_steps, max_iter)
            output_steps.pop(-1)

            output_steps.append("W")
            output2 = recur(step_size * 2, (curr_pos[0] - 1, curr_pos[1]), target, output_steps, max_iter)
            output_steps.pop(-1)

        else:
            output_steps.append("N")
            output1 = recur(step_size * 2, (curr_pos[0], curr_pos[1] + 1), target, output_steps, max_iter)
            output_steps.pop(-1)

            output_steps.append("S")
            output2 = recur(step_size * 2, (curr_pos[0], curr_pos[1] - 1), target, output_steps, max_iter)
            output_steps.pop(-1)

        # print(output1, output2)
        if output1 is not None:
            if output2 is not None:
                if len(output1) > len(output2):
                    return output2
                return output1
            return output1
        return output2


    results = []
    for direction in "EWNS":
        if direction == "E":
            output_steps.append("E")
            output = recur(step_size * 2, (curr_pos[0] + step_size, curr_pos[1]), target, output_steps, max_iter)

        elif direction == "W":
            output_steps.append("W")
            output = recur(step_size * 2, (curr_pos[0] - step_size, curr_pos[1]), target, output_steps, max_iter)

        elif direction == "N":
            output_steps.append("N")
            output = recur(step_size * 2, (curr_pos[0], curr_pos[1] + step_size), target, output_steps, max_iter)

        elif direction == "S":
            output_steps.append("S")
            output = recur(step_size * 2, (curr_pos[0], curr_pos[1] - step_size), target, output_steps, max_iter)
        output_steps.pop(-1)

        if output is not None:
            results.append(output)

    # print(results)
    n_len = int(math.log(max(abs(x), abs(y)), 2)) + 2
    # print(n_len)
    best_result = None
    for result in results:
        if len(result) <= n_len:
            best_result = result
            n_len = len(result)
    # print("best result {}".format(best_result))
    return best_result



if __name__ == '__main__':

    t = int(input())
    for testcase_i in range(1, t + 1):
        x, y = input().split(" ")
        ans = p1(int(x), int(y))
        print("Case #{}: {}".format(testcase_i, ans))
