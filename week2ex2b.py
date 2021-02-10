#Week2 exercise 2 B#

import csv
import sys
import argparse

def write_list_to_file_cli(output_file, *lst):
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
    parser.add_argument('-a','--file')
    parser.add_argument('--lst', required=True)

    args = parser.parse_args()

    if args.output:
        print('Det her er hjælpe teksten')
    if args.file:
        with open(args.file, 'a') as file_obj:
            lst = args.lst
            for item in lst:
                file_obj.write(item)
    else: 
        print(lst)

if __name__ == '__main__':
    write_list_to_file_cli(*sys.argv[1:])