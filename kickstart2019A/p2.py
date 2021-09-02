def get_manhattan_distance(point1, point2):
    r1, c1 = point1
    r2, c2 = point2
    return abs(r1 - r2) + abs(c1 - c2)


def p2(matrix, r, c):
    offices = []
    grounds = []
    for r_i in range(r):
        for c_i in range(c):
            if matrix[r_i][c_i] == '1':
                offices.append((r_i, c_i))
            else:
                grounds.append((r_i, c_i))

    if len(grounds) < 2:
        return 0

    min_dists = [r + c for _ in grounds]
    for i, ground in enumerate(grounds):
        for office in offices:
            dist = get_manhattan_distance(ground, office)
            min_dists[i] = min(dist, min_dists[i])

    n = len(grounds)
    overall_min_dist = r + c
    for i in range(n):
        office_to_be = grounds[i]
        current_min_dists = []
        for j in range(n):
            if i != j:
                dist = get_manhattan_distance(office_to_be, grounds[j])
                current_min_dists.append(min(dist, min_dists[j]))
        
        if len(current_min_dists) > 0:
            current_overall_min_dist = max(current_min_dists)
            if current_overall_min_dist < overall_min_dist:
                overall_min_dist = current_overall_min_dist

    return overall_min_dist


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r, c = input().split(" ")
        r = int(r)
        c = int(c)
        matrix = []
        for _ in range(r):
            row = input()
            matrix.append(row)

        ans = p2(matrix, r, c)
        print("Case #{}: {}".format(i, ans))
