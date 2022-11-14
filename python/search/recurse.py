# -*- coding: utf-8 -*-


def recurse(input, front_to_back):
    if len(input) == 0:
        print('done')
        return

    print(f'{input}')

    if front_to_back:
        recurse(input[1:], front_to_back)
    else:
        recurse(input[:-1], front_to_back)


if __name__ == '__main__':
    s = 'abcdefghijk'
    recurse(s, True)
    recurse(s, False)

