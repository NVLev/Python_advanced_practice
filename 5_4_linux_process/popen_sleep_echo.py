import subprocess


# мы хотим соединить два процесса, воссоздав поведение конвейера (pipe) оболочки sleep_process | echo_process
# Как мы
# знаем, когда передаем две команды в оболочку, стандартный вывод той, что находится слева от пайпа «|», используется
# как стандартный ввод той, которая находится справа. В приведенном ниже примере результат выполнения двух связанных
# конвейером команд сохраняется в переменной:

def main():
    """
    Simulates the command 'sleep 15 && echo "My mission is done here!"' using Popen.
    """
    sleep_process = subprocess.Popen(['sleep', '15'], stdout=subprocess.PIPE)
    echo_process = subprocess.Popen(['echo', 'My mission is done here!'], stdin=sleep_process.stdout)
    sleep_process.stdout.close()
    output = echo_process.communicate()


if __name__ == '__main__':
    main()
