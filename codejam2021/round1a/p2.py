from typing import List, Dict


def get_primes():
    prime_str = "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499"  # noqa
    primes = prime_str.split(", ")
    primes = [int(prime) for prime in primes]
    return primes


def get_prime_factorization(prime_candidates: List[int], target_val: int):
    output = {}
    current_val = target_val
    while current_val > 1:
        for prime in prime_candidates:
            if current_val % prime == 0:
                if prime not in output:
                    output[prime] = 1
                else:
                    output[prime] += 1
                current_val = current_val / prime
                break
    return output


# def is_valid_product(prime2num: Dict[int, int], prime_fact: Dict[int, int]):
#     for prime, num in prime_fact.items():
#         if prime not in prime2num:
#             return False
#         if num > prime2num[prime]:
#             return False
#     return True


def is_valid_product(prime2num: Dict[int, int], target_val):
    prime2num = prime2num.copy()
    current_val = target_val
    prime_sum = 0
    while current_val > 1:
        flag = False
        for prime, num in prime2num.items():
            if current_val % prime == 0:
                flag = True
                if num > 0:
                    current_val = current_val / prime
                    prime2num[prime] -= 1
                    prime_sum += prime
                    break
                else:
                    return False, -1
        if not flag:
            return False, -1
    return True, prime_sum


def main(prime2num: Dict[int, int]):
    total_sum = 0
    for prime, num in prime2num.items():
        total_sum += prime * num

    # prime_candidates = get_primes()

    for cand_val in range(total_sum, 1, -1):
        # prime_fact = get_prime_factorization(
        #     prime_candidates=prime_candidates,
        #     target_val=cand_val,
        # )
        valid_product, prime_fact_sum = is_valid_product(
            prime2num=prime2num,
            target_val=cand_val,
        )
        if not valid_product:
            continue

        # prime_fact_sum = 0
        # for prime, num in prime_fact.items():
        #     prime_fact_sum += prime * num

        res_prime_sum = total_sum - prime_fact_sum
        if res_prime_sum != cand_val:
            continue

        if res_prime_sum == cand_val:
            return cand_val

    return 0


if __name__ == "__main__":
    n_cases = int(input())
    for case_i in range(1, n_cases + 1):
        M = int(input())
        prime2num = {}
        for _ in range(M):
            prime, num = input().split(" ")
            prime2num[int(prime)] = int(num)
        result = main(prime2num)
        print("Case #{}: {}".format(case_i, result))

    # prime2num = {}
    # primes = get_primes()[0: 3]
    # for prime in primes:
    #     prime2num[prime] = 100
    # result = main(prime2num)
    # print(result)

    # # result = get_prime_factorization(prime_candidates=get_primes(), target_val=120)
    # # print(result)
