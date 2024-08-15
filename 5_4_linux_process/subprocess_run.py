import subprocess


def run_program():
    res = subprocess.Popen(['python', 'ps_a_commandd.py'])
    print(res)


if __name__ == '__main__':
    run_program()
