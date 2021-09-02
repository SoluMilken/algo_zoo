from typing import List
import random


def append_sort(prevX: str, currentX: str):
    if len(prevX) < len(currentX):
        # print("<")
        return currentX, 0
    elif len(prevX) == len(currentX):
        # print("==", prevX, currentX)
        if int(prevX) < int(currentX):
            # print(prevX, "<" ,currentX)
            return currentX, 0
        return currentX + "0", 1
    else:
        # print(">")
        prefix_prevX = prevX[: len(currentX)]
        if int(prefix_prevX) == int(currentX):
            suffix_prevX = prevX[len(currentX) :]
            new_suffix_currentX = str(int(suffix_prevX) + 1)
            if len(new_suffix_currentX) > len(suffix_prevX):
                return prevX + "0", len(prevX) - len(currentX) + 1
            new_currentX = str(
                int(prefix_prevX) * (10 ** (len(prevX) - len(currentX)))
                + int(new_suffix_currentX)
            )
            # print(new_currentX)
            return (new_currentX, len(prevX) - len(currentX))

        elif int(prefix_prevX) > int(currentX):
            return (
                currentX + "0" * (len(prevX) - len(currentX) + 1),
                len(prevX) - len(currentX) + 1,
            )

        else:
            return (
                currentX + "0" * (len(prevX) - len(currentX)),
                len(prevX) - len(currentX),
            )


def main(X: List[str]):
    count = 0
    # print(X)
    for idx in range(1, len(X)):
        # print(X[idx - 1], X[idx])
        new_currentX, new_count = append_sort(
            prevX=X[idx - 1],
            currentX=X[idx],
        )
        count += new_count
        X[idx] = new_currentX
        # print(X)
    return count, X


def gen_X_n_Y(N):
    Y = sorted(random.sample(range(1000000000), N))
    Y = [str(y) for y in Y]
    X = []
    count = 0
    for i, y in enumerate(Y):
        if i % 2 == 1:
            k = random.randint(1, len(y))
            x = y[:k]
            X.append(x)
            count += len(y) - len(x)
        else:
            X.append(y)
    return X, Y, count


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        N = int(input())
        X = [num for num in input().split(" ")]
        result = main(X)
        print("Case #{}: {}".format(case_i, result[0]))
    # for _ in range(100):
    #     X, Y, count = gen_X_n_Y(N=7)
    #     result, newX = main(X.copy())
    #     if result > count:
    #         print(X, Y, count)
    #         print(newX, result)
