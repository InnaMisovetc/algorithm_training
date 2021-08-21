from math import sqrt


def eq_solution(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    elif a == 0:
        if b < 0 or sqrt(b) != c:
            return 'NO SOLUTION'
        else:
            return 'MANY SOLUTIONS'
    else:
        x = (c ** 2 - b) / a
        if int(x) == x:
            return int(x)
        else:
            return 'NO SOLUTION'


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(eq_solution(a, b, c))


if __name__ == '__main__':
    main()
