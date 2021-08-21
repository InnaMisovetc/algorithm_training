def temp_after_one_hour(t_room, t_cond, mode):
    if mode == 'fan':
        return t_room
    elif mode == 'auto':
        return t_cond
    elif mode == 'freeze':
        if t_cond < t_room:
            return t_cond
        else:
            return t_room
    elif mode == 'heat':
        if t_cond > t_room:
            return t_cond
        else:
            return t_room


def main():
    t_room, t_cond = map(int, input().split(' '))
    mode = input()
    print(temp_after_one_hour(t_room, t_cond, mode))


if __name__ == '__main__':
    main()
