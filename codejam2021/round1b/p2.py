from typing import List
from collections import deque
import math

"""
Subtransmutation (13pts, 18pts)
"""


def break_or_not(val: int, status: List[int], Us: List[int]):
    if val > len(Us):
        return True
    if Us[val - 1] == 0:
        # do not need val
        return True
    diff = Us[val - 1] - status[val - 1]
    if diff == 0:
        # already fulfilled
        return True
    return False


def bfs(ans: int, A: int, B: int, Us: List[int]):
    q = deque()
    q.append(ans)
    status = [0 for _ in range(len(Us))]
    while len(q) > 0:
        # print(q, status)
        if status == Us:
            return True
        node = q.popleft()
        if node <= len(Us):
            status[node - 1] -= 1
        if not break_or_not(val=node, status=status, Us=Us):
            status[node - 1] += 1
        else:
            for cand in [node - A, node - B]:
                if cand > 0:
                    q.append(cand)
                    if cand <= len(Us):
                        status[cand - 1] += 1

    return False


def main(N: int, A: int, B: int, Us: List[int]):
    n_metals = sum(Us)
    height = int(math.log(n_metals, 2))
    min_ans = len(Us) + min(A, B)
    max_ans = len(Us) + (A + B) * height
    for ans in range(min_ans, max_ans + 1):
        if bfs(ans=ans, A=A, B=B, Us=Us):
            return ans
    return "IMPOSSIBLE"


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N, A, B = input().split(" ")
        N, A, B = int(N), int(A), int(B)
        Us = [int(Ui) for Ui in input().split(" ")]
        result = main(N, A, B, Us)
        print("Case #{}: {}".format(case_i, result))
