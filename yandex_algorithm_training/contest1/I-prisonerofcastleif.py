def escape(sides, side, first_name, second_name, first, second):
    if first_name not in sides and side <= first:
        sides.append(first_name)
    elif second_name not in sides and side <= second:
        sides.append(second_name)


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    sides = []
    for side in [A, B, C]:
        if D < E:
            escape(sides, side, 'D', 'E', D, E)
        else:
            escape(sides, side, 'E', 'D', E, D)
    if 'D' in sides and 'E' in sides:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
