from os import walk, mkdir
from os.path import splitext, abspath, join
from argparse import ArgumentParser
from urllib.parse import urlsplit, urlunsplit

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

def group_urls(urls):
    result = dict()
    for u in urls:
        data = urlsplit(u)
        if data.netloc in result:
            result[data.netloc].append(urlunsplit(data))
        else:
            result[data.netloc] = [urlunsplit(data)]
    print(result.keys())
    return result

def write_grouped_urls(target_dir, urls):
    try:
        mkdir(join(abspath(target_dir), 'output'))
    except OSError:
        print(f'Cannot create {target_dir}/output')
    for keys, values in urls.items():
        with open(f"{join(abspath(target_dir), 'output', keys.replace('.', '_'))}.txt", 'w') as w:
            for v in values:
                w.write(f'{v}\n')


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
            grouped_urls = group_urls(parsed_data)
            write_grouped_urls(args.pd, grouped_urls)

