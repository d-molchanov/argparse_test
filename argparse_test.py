from os import walk
from os.path import splitext, abspath, join
from argparse import ArgumentParser
from urllib.parse import urlparse

def parse_files(files):
    all_lines = []
    for filename in files:
        try:
            with open(filename, 'r') as f:
                data = [el.rstrip() for el in f.readlines() if el != '\n']
                all_lines += data
        except IOError:
            print(f'Check {filename} - something wrong!')    
    return all_lines

def filter_files_by_extention(files, ext):
    result = []
    for f in  files:
        f_name, f_ext = splitext(f)
        if f_ext == ext or (f_name.endswith(f'.{ext}') and f_ext == ''):
            result.append(f)
    return result



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--pd')
    parser.add_argument('--ext')
    args = parser.parse_args()
    files = []
    if args.pd:
        files = next(walk(args.pd))[2]
    if args.ext:
        if files:
            ext_files = filter_files_by_extention(files, args.ext)
            print(f'*.{args.ext} files:')
            for i, el in enumerate(ext_files, 1):
                print(i, el, sep='\t')
            abs_files = [join(abspath(args.pd), f) for f in ext_files]
            parsed_data = parse_files(abs_files)
            for data in parsed_data:
                print(data)

