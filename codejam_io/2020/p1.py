def main(S: str) -> int:
    I = 0
    i = 0
    nIO = 0
    for ele in S:
        if ele == "I":
            I += 1
        elif ele == "i":
            i += 1
        elif ele == "o":
            if i > 0:
                i -= 1
            else:
                I -= 1
        else:
            if I > 0:
                nIO += 1
                I -= 1
            else:
                i -= 1
    return nIO


if __name__ == "__main__":
    T = int(input())
    for case_i in range(1, T + 1):
        S = input()
        result = main(S)
        print("Case #{}: {}".format(case_i, result))
    # inputs = """IiOioIoO
    # IiOOIo
    # IoiOiO
    # io
    # IIIIOOOO"""
    # for input_str in inputs.split("\n"):
    #     print(input_str)
    #     print(main(input_str))
