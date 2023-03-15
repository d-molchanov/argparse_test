from os import walk
from os.path import splitext, abspath
from argparse import ArgumentParser



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--pd')
    parser.add_argument('--ext')
    args = parser.parse_args()
    files = None
    if args.pd:
        files = next(walk(args.pd))[2]
    if args.ext:
        if files:
            ext_files = [el for el in files if splitext(el)[1] == f'.{args.ext}' or (splitext(el)[0].endswith('.txt') and splitext(el)[1] == '')]
            print(f'*.{args.ext} files:')
            for i, el in enumerate(ext_files, 1):
                print(i, el, sep='\t')
            if ext_files:
                all_lines = []
                for f in ext_files:
                    print(f'{args.pd}/{f}')
                    # try:
                    #     with open(f'./{args.pd}/{f}' 'r') as _f:
                    #         data = [el for el in _f.readlines() if el]
                    #         all_lines += data
                    # except IOError:
                    #     print(f'Check {f} - something wrong!')
                for line in all_lines:
                    print(line)
