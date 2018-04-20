from pinmix.filler import process_file
import sys


def main():
    args = sys.argv
    if len(args) > 1:
        filename = args[1]
    else:
        raise Exception("Pass arguments to script!")
    process_file(filename)


if __name__ == '__main__':
    main()
