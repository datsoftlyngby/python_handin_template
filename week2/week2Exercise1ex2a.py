#Week2 exercise 2 A#

import csv
import sys


def write_arb_to_file(output_file, *tekst):
    with open(output_file, 'a') as file:
        write = csv.writer(file)
        write.writerow(strings)


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    write_arb_to_file(*sys.argv[1:])