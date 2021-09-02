def iter_binary_search(sorted_arr, target):
    n = len(sorted_arr)
    left = 0
    right = n - 1

    while right >= left:
        half = (right + left) // 2

        if sorted_arr[half] == target:
            return half

        if sorted_arr[half] > target:
            right = half - 1

        if sorted_arr[half] < target:
            left = half + 1

    return -1


def recur_binary_search(sorted_arr, target):
    left = 0
    right = len(sorted_arr) - 1
    return search(left, right, target, sorted_arr)


def search(left, right, target, sorted_arr):
    if left > right:
        return -1

    half = (left + right) // 2

    if sorted_arr[half] == target:
        return half

    if sorted_arr[half] > target:
        return search(left, half - 1, target, sorted_arr)

    if sorted_arr[half] < target:
        return search(half + 1, right, target, sorted_arr)


if __name__ == "__main__":
    sorted_arr = [-1, 1, 2, 3, 4, 5, 1e10]
    target = 7

    print(iter_binary_search(sorted_arr, target))
    print(recur_binary_search(sorted_arr, target))
