import sys

def main():
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)
    # user_input = input()
    # print('User input: "{}"'.format(user_input))


if __name__ == '__main__':
    main()
