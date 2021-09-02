def ft_int_binary_search(func, start, end):
    """
    FFTTT -> return 2
    start F
    end T
    """
    if end - start == 1:
        return end

    mid = int((end + start) / 2.0)
    if func(mid):
        return int_binary_search(
            func=func,
            start=start,
            end=mid,
        )
    else:
        return int_binary_search(
            func=func,
            start=mid,
            end=end,
        )


def tf_int_binary_search(func, start, end):
    """
    TTTFF -> return 2
    start T
    end F
    """
    if end - start == 1:
        return end

    mid = int((end + start) / 2.0)
    if func(mid):
        return int_binary_search(
            func=func,
            start=mid,
            end=end,
        )
    else:
        return int_binary_search(
            func=func,
            start=start,
            end=mid,
        )

# def fool(num):
#     if (num > 10):
#         return True
#     else:
#         return False


# if __name__ == '__main__':
#     print(int_binary_search(func=lambda x: x > 10, start=0, end=100))
