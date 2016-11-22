import os
import argparse
import gen_string
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process create dirs for nginx configurations')
    parser.add_argument(
        '--path', help='path to parent dir of all cache dirs', default='/home/test', required=False)
    parser.add_argument('--count', type=int, help='count dirs', default=5, required=False)
    parser.add_argument('--length', type=int,
                        help='length of dirs name ', default=10, required=False)

    args = parser.parse_args()
    parent_path = args.path
    count = args.count
    length = args.length
    i = 0
    list_names = []
    flag = input('Are you sure to create {0} dirs in {1} -- Answer : y/n (Default no)'.format(count, parent_path))
    if len(flag) > 0 and flag[0] !=  'y':
        sys.exit(0)

    while i < count:
        name = gen_string.random_string(length, True, True, True)
        path = parent_path + '/' + name
        if not os.path.exists(path):
            os.makedirs(path)
            i += 1
