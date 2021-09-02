def p2(u, input_dict, chars):
    assert len(chars) == 10
    chars_dict = CharsDict(chars)

    for key, values in input_dict.items():

        for value in values:
            key_str = str(key)
            if len(value) != len(key_str):
                continue
            str_len = len(key_str)

            if len(set(value)) == 1:
                chars_dict.intersection(
                    key=value[0],
                    target_set=set(range(1, min([int(k) for k in key_str]) + 1)),
                )

            for digit_i in range(str_len):
                chars_dict.intersection(
                    key=value[digit_i],
                    target_set=set(range(1, int(key_str[digit_i]) + 1)),
                )
                if chars_dict.get_value(key=value[digit_i]) != {int(key_str[digit_i])}:
                    break

            if chars_dict.done():
                return chars_dict.output_ans()

    return chars_dict.output_ans()


class CharsDict:

    def __init__(self, chars):
        self.inner_dict = {char: set(range(0, 10)) for char in chars}

    def intersection(self, key, target_set):
        self.inner_dict[key] = self.inner_dict[key].intersection(target_set)
        if len(self.inner_dict[key]) == 1:
            for k, v in self.inner_dict.items():
                if k != key:
                    self.inner_dict[k] = self.inner_dict[k] - self.inner_dict[key]

    def print(self):
        print(self.inner_dict)

    def done(self):
        for k, v in self.inner_dict.items():
            if len(v) != 1:
                return False
        return True

    def output_ans(self):
        output_list = ["O" for _ in range(10)]
        for k, v in self.inner_dict.items():
            ind = list(v)[0]
            output_list[ind] = k
        return "".join(output_list)

    def get_value(self, key):
        return self.inner_dict[key]



if __name__ == '__main__':

    t = int(input())
    for testcase_i in range(1, t + 1):
        u = int(input())
        input_dict = {}
        chars = set()
        for _ in range(10 ** 4):
            m, r = input().split(" ")

            if int(m) == -1:
                continue

            if len(m) != len(r):
                continue

            if int(m) not in input_dict:
                input_dict[int(m)] = set()
                input_dict[int(m)].add(r)
            else:
                input_dict[int(m)].add(r)

            chars = chars.union(set(r))
        ans = p2(u, input_dict, chars)
        print("Case #{}: {}".format(testcase_i, ans))
