def a(num):
    for i in range(1, num + 1):
        # print(int(((i / num) * 1000)))
        if int(((i / num) * 1000)) % 10 >= 5:
            print(i)

if __name__ == '__main__':
    a(num=121)
