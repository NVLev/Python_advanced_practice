import sys
# Напишите функцию, которая с помощью subprocess будет запускать команду:
# $ curl -i -H "Accept: application/json" -X GET
# https://api.ipify.org?format=json
# Токенизируйте через shlex, распарсите вывод и верните строку — IP-адрес.

def main():
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)
    # user_input = input()
    # print('User input: "{}"'.format(user_input))


if __name__ == '__main__':
    main()
