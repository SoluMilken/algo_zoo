# def solution(S):
#     record = {}
#     for char in S:
#         if char not in record:
#             record[char] = 1
#         else:
#             record[char] += 1

#     freqs = record.values()

#     stat = {}
#     for num in freqs:
#         if num not in stat:
#             stat[num] = 1
#         else:
#             stat[num] += 1

#     if len(stat) == len(record):
#         return 0

#     stat_tuple = list(reversed(sorted(stat.items())))

#     for key, num in stat_tuple:
#         if (key > 0) and (num > 1):
#             stat[key] = 1
#             end_key = max((key - num), 0)
#             for sub_key in range(key - 1, end_key, -1):
#                 if sub_key not in stat:
#                     stat[sub_key] = 1
#                 else:
#                     stat[sub_key] += 1
#             stat_tuple = list(reversed(sorted(stat.items())))

#     return sum(freqs) - sum(stat.keys())


# def solution(S):
#     freqs = [0 for _ in range(26)]
#     for char in S:
#         freqs[ord(char) - ord('a')] += 1

#     nonzero_freqs = []
#     for freq in freqs:
#         if freq != 0:
#             nonzero_freqs.append(freq)
#     freqs = nonzero_freqs

#     if len(set(freqs)) == len(freqs):
#         return 0

#     stat = {}
#     for freq in freqs:
#         if freq not in stat:
#             stat[freq] = 1
#         else:
#             stat[freq] += 1

#     while (sum(stat.values()) != len(stat)):
#         sorted_stat_tuple = list(reversed(sorted(stat.items())))
#         # print(sorted_stat_tuple)
#         for freq, num in sorted_stat_tuple:
#             if num > 1:
#                 stat[freq] = 1
#                 for i in range(freq - 1, max((freq - num), 0), -1):
#                     if i not in stat:
#                         stat[i] = 1
#                     else:
#                         stat[i] += 1
#             # print(stat)
#     return sum(freqs) - sum(stat.keys())


def solution(S):

    freq_dict = {}
    for char in S:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1

    freq_list = list(freq_dict.values())

    freq_list.sort()
    freq_list.reverse()

    result = 0
    prev = 300000
    for x in freq_list:
        # print(x, prev, result)
        if x >= prev:
            prev = max(prev - 1, 0)
            result += x - prev
        else:
            prev = x

    return result


if __name__ == "__main__":
    # print(solution("a" * 1000 + "b" * 1000 + "c" * 1000))
    print(solution("zzzzzaaabbbcccdddeeffggh"))
