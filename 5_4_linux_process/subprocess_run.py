import subprocess


def run_program():
    res = subprocess.run(['python', 'test_curl.py'], stderr=subprocess.STDOUT)
    print(res)


if __name__ == '__main__':
    run_program()
