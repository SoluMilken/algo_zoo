# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Point2D  # library with types used in the task


def solution(A):
    # write your code in Python 3.6
    record_set = set()

    for point in A:

        if (point.x == 0) or (point.y == 0):  # axis
            slope = 0

            if (point.x > 0) and (point.y == 0):  # +x
                phase = 5

            if (point.x == 0) and (point.y > 0):  # +y
                phase = 6

            if (point.x < 0) and (point.y == 0):  # -x
                phase = 7

            if (point.x == 0) and (point.y < 0):  # -y
                phase = 8

        else:
            slope = point.y / point.x

            if (point.x > 0) and (point.y > 0):  # first quadrant
                phase = 1

            if (point.x < 0) and (point.y > 0):  # second quadrant
                phase = 2

            if (point.x < 0) and (point.y < 0):  # third quadrant
                phase = 3

            if (point.x > 0) and (point.y < 0):  # forth quadrant
                phase = 4

        record_set.add((slope, phase))

    return len(record_set)
