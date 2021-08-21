def triangle(one, second, third):
    if one >= second + third or second >= one + third or third >= one + second:
        return 'NO'
    return 'YES'


def main():
    one_side = int(input())
    second_side = int(input())
    third_side = int(input())
    print(triangle(one_side, second_side, third_side))


if __name__ == '__main__':
    main()
