



def get_player_win_rate(record):
    n_win = 0
    for result in record:
        if result == "1":
            n_win += 1
    return n_win / len(record)


def get_player_skill_levels(records):
    skill_levels = []
    for record in records:
        win_rate = get_player_win_rate(record)
        skill_levels.append(-3 + 6 * win_rate)
    return skill_levels


def get_problem_difficulty_levels(records):
    difficulty_levels = []
    n_problems = len(records[0])
    for problem_i in range(n_problems):
        n_correct = 0
        for record in records:
            if record[problem_i] == "1":
                n_correct += 1
        correct_rate = n_correct / len(records)
        difficulty_levels.append(-3 + 6 * correct_rate)
    return difficulty_levels


def main(records):
    skill_levels = get_player_skill_levels(records)
    difficulty_levels = get_problem_difficulty_levels(records)

    for si in skill_levels:




# def get_question_correct_rate(records, user_ids):
#     correct_rate = []
#     for problem_i in range(len(records[0])):
#         n_correct = 0
#         for user_id in user_ids:
#             if records[user_id][problem_i] == "1":
#                 n_correct += 1
#         correct_rate.append(n_correct / len(user_ids))
#     return correct_rate


# def get_candidate_players(records):
#     players = []
#     for player_i, record in enumerate(records):
#         win_rate = get_player_win_rate(record)
#         # print(player_i, win_rate)
#         if win_rate >= 0.5:
#             players.append(player_i)
#     return players


# def get_cheater(records, user_ids, easy_questions):
#     player2nCorrect = []

#     for user_id in user_ids:
#         record = records[user_id]
#         n_correct = 0
#         for problem_i in easy_questions:
#             if record[problem_i] == "1":
#                 n_correct += 1
#         player2nCorrect.append((user_id, n_correct))

#     min_n_correct = len(easy_questions)
#     cheater = None
#     for player_i, n_correct in player2nCorrect:
#         if n_correct < min_n_correct:
#             min_n_correct = n_correct
#             cheater = player_i
#     return cheater



def main(records):
    s_lst = get_player_win_rate()
    candidates = get_candidate_players(records)
    correct_rates = get_question_correct_rate(records, candidates)

    easy_questions = []
    hard_questions = []
    for problem_i, correct_rate in enumerate(correct_rates):
        if correct_rate > 0.5:
            easy_questions.append(problem_i)
        else:
            hard_questions.append(problem_i)
    return get_cheater(records, candidates, easy_questions)


# if __name__ == '__main__':
#     n_cases = int(input())
#     P = int(input())
#     for case_i in range(1, n_cases + 1):
#         records = []
#         for j in range(100):
#             record = input()
#             records.append(record)
#         result = main(records)
#         print("Case #{}: {}".format(case_i, result))


import random
import math


qs = []
for _ in range(10000):
    qs.append(random.uniform(-3, 3))

s = []
for _ in range(100):
    s.append(random.uniform(-3, 3))

# for player_i, si in enumerate(s):
#     total_sum = 0
#     for q in qs:
#         total_sum += 1 / (1 + math.exp(- si + q))
#     print("player {}, s = {}, sum = {}".format(player_i, si, total_sum))

nPlayerCorrect2Qi = {}
for _ in range(100):

    qs = []
    for _ in range(10000):
        qs.append(random.uniform(-3, 3))

    s = []
    for _ in range(100):
        s.append(random.uniform(-3, 3))

    q2sumS = []
    for q in qs:
        sumS = 0
        for si in s:
            sumS += 1 / (1 + math.exp(- si + q))

        if int(sumS) not in nPlayerCorrect2Qi:
            nPlayerCorrect2Qi[int(sumS)] = [q]
        else:
            nPlayerCorrect2Qi[int(sumS)].append(q)

for nPlayer, qis in nPlayerCorrect2Qi.items():
    nPlayerCorrect2Qi[nPlayer] = sum(qis) / len(qis)

import pdb; pdb.set_trace()
print(nPlayerCorrect2Qi)

