def argmin(iterable):
    return min(enumerate(iterable), key=lambda x: x[1])[0]


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    all_flavors = list(range(N))
    record = [0] * N
    for _ in range(N):
        prefs = [int(s) for s in input().split(" ")]
        num_prefs = prefs[0]
        prefs = prefs[1:]
        for p in prefs:
            record[p] += 1
        candidates = list(set(all_flavors).intersection(set(prefs)))
        if (num_prefs == 0) or (len(candidates) == 0):
            print(-1, flush=True)
        else:
            chosen = candidates[argmin([record[j] for j in candidates])]
            all_flavors.remove(chosen)
            print(chosen, flush=True)
