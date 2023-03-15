from os import walk
from argparse import ArgumentParser



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--ls')
    args = parser.parse_args()
    if args.ls:
        print(next(walk(args.ls))[2])
