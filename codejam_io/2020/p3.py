from typing import List


def main(S: str) -> int:
    return dfs(S, 0, [0, 0, 0, 0], 0, 0)


def dfs(S: str, idx: int, visited: List[int], i: int, I: int):
    """
    visited io iO Io IO
    """
    ele = S[idx]
    if idx == len(S) - 1:
        if ele == "O":
            if I > 0:
                # print(S, idx, visited, i, I, 1)
                return 1
        # print(S, idx, visited, i, I, 0)
        return 0

    if ele == "o":
        i_result = -1
        I_result = -1
        if i > 0 and visited[0] == 0:
            i -= 1
            visited[0] = 1
            i_result = dfs(S, idx + 1, visited, i, I)
            # print("io", S, idx + 1, visited, i, I, i_result)
            visited[0] = 0
            i += 1
        if I > 0 and visited[2] == 0:
            I -= 1
            visited[2] = 1
            I_result = dfs(S, idx + 1, visited, i, I)
            # print("Io", S, idx + 1, visited, i, I, i_result)
            visited[2] = 0
            I += 1
        return max(i_result, I_result)

    elif ele == "O":
        i_result = -1
        I_result = -1
        if i > 0 and visited[1] == 0:
            i -= 1
            visited[1] = 1
            i_result = dfs(S, idx + 1, visited, i, I)
            # print("iO", S, idx + 1, visited, i, I, i_result)
            visited[1] = 0
            i += 1
        if I > 0 and visited[3] == 0:
            I -= 1
            visited[3] = 1
            I_result = dfs(S, idx + 1, visited, i, I)
            # print("IO", S, idx + 1, visited, i, I, I_result + 1)
            visited[3] = 0
            I += 1
            if I_result > 0:
                I_result += 1
        return max(i_result, I_result)

    else:
        for idx_i in range(idx, len(S)):
            if S[idx_i] in ["o", "O"]:
                break
            if S[idx_i] == "i":
                i += 1
            elif S[idx_i] == "I":
                I += 1
        for vi in range(4):
            visited[vi] = 0
        # print(idx, i, I)
        return dfs(S, idx_i, visited, i, I)


if __name__ == "__main__":
    # T = int(input())
    # for case_i in range(1, T + 1):
    #     S = input()
    #     result = main(S)
    #     print("Case #{}: {}".format(case_i, result))
    inputs = """IiOioIoO
    IIOiOo
    IoiOiO
    io
    IiOIOIoO"""
    for input_str in inputs.split("\n"):
        print(input_str, main(input_str))
