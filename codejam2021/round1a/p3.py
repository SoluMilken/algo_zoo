from typing import List, Dict


def reverse_x(x: str):
    output = []
    for ans in x:
        if ans == "T":
            output.append("F")
        else:
            output.append("T")
    return "".join(output)


def main(X: List[str], Y: List[int]):
    opt_x = ""
    opt_y = 0
    for x, y in zip(X, Y):
        if y > opt_y:
            opt_y = y
            opt_x = x
        rev_x = reverse_x(x)
        rev_y = len(x) - y
        if rev_y > opt_y:
            opt_y = rev_y
            opt_x = rev_x
    return f"{opt_x} {opt_y}/1"


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N, Q = input().split(" ")
        N, Q = int(N), int(Q)
        X = []
        Y = []
        for _ in range(N):
            x, y = input().split(" ")
            X.append(x)
            Y.append(int(y))
        result = main(X, Y)
        print("Case #{}: {}".format(case_i, result))

    # prime2num = {}
    # primes = get_primes()[0: 3]
    # for prime in primes:
    #     prime2num[prime] = 100
    # result = main(prime2num)
    # print(result)

    # # result = get_prime_factorization(prime_candidates=get_primes(), target_val=120)
    # # print(result)
