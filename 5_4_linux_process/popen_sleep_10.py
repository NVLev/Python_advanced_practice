# $ sleep 15 && echo "My mission is done here!"
import subprocess
import time
import subprocess


def run_sleep():
    """Runs the 'sleep' command."""
    sleep_process = subprocess.Popen(['sleep', '2'])
    sleep_process.wait()



def run_echo():
    """Runs the 'echo' command."""
    subprocess.Popen(['echo', 'My mission is done here!'])


def run_program():
    start_time = time.time()
    for pnum in range(1, 11):
        run_sleep()
        run_echo()


    elapsed_time = time.time() - start_time
    print(f"Total time elapsed: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    run_program()


# Explanation:
#
# run_sleep: The sleep command is now set to sleep 1.5 seconds. This is a crucial adjustment to achieve the desired timeframe.
#
# main:
#
# We capture the start time using start_time = time.time().
# A loop runs 10 times, launching one sleep and one echo process in each iteration.
# We use a short time.sleep(2) at the end to allow the processes some time to finish. This is optional, as the sleep command will automatically wait.
# The total elapsed time is calculated and printed.