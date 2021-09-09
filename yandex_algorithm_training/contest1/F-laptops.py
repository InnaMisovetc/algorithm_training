def main():
    a1, b1, a2, b2 = map(int, input().split(' '))
    x = [a1, b1]
    y = [a2, b2]
    s = 2 * (10**6)
    for i in range(2):
        for k in range(2):
            new_s1 = max(x.pop(i), y.pop(k))
            new_s2 = x[0] + y[0]
            new_s = new_s1 * new_s2
            if new_s <= s:
                s = new_s
                s1 = new_s1
                s2 = new_s2
            x = [a1, b1]
            y = [a2, b2]
    print(s1, s2)


if __name__ == '__main__':
    main()
