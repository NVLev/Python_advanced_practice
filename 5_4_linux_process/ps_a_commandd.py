import subprocess


def main():
    """
  Executes the `ps -A` command, counts the processes, and prints the result.
  """
    # Execute the ps -A command
    process = subprocess.run(["ps", "-A"], capture_output=True, text=True)
    # Get the output as a string
    output = process.stdout
    # Split the output into lines
    lines = output.splitlines()
    # Count the processes
    process_count = 0
    for line in lines:
        # Skip the header line
        if line.startswith("  "):
            process_count += 1
    # Print the number of processes
    print(f"There are {process_count} processes running.")


if __name__ == '__main__':
    main()
