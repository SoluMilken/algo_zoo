from typing import List, Dict


def main():
    pass


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N = int(input())
        X = [num for num in input().split(" ")]
        result = main(X)
        print("Case #{}: {}".format(case_i, result[0]))
