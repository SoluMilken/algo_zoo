import random

from p2 import p2


def check_p2(input_str, result_from_p2):

    # 1 remove all ()
    tx_str = result_from_p2.replace("(", "")
    tx_str = tx_str.replace(")", "")
    assert tx_str == input_str

    # check parathesis
    stack = []
    for char in result_from_p2:
        if char == "(":
            stack.append("(")
        elif char.isdigit():
            assert len(stack) == int(char)
        else: # ")"
            stack.pop()
    assert len(stack) == 0



if __name__ == '__main__':
    T = 100
    S = 100

    for t in range(T):
        s_len = random.randint(1, 100)
        rand_ints = [str(random.randint(0, 1)) for _ in range(s_len)]
        input_str = "".join(rand_ints)
        # print(input_str)
        result = p2(input_str)
        check_p2(input_str, result)
