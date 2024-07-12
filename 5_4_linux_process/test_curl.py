# Напишите функцию, которая с помощью subprocess будет запускать команду:
# $ curl -i -H "Accept: application/json" -X GET
# https://api.ipify.org?format=json
# Токенизируйте через shlex, распарсите вывод и верните строку — IP-адрес.
import sys
import subprocess
import shlex
import json


def main():
    """
    Executes a curl command to get the user's IP address, parses the JSON output,
    and returns the IP address as a string.
    Returns:
        str: The user's IP address.
    """
    command = ["curl", "-i", "-H", "Accept: application/json", "-X", "GET",
               "https://api.ipify.org?format=json"]
    # Tokenize the command using shlex for safer command execution
    tokenized_command = shlex.split(" ".join(command))
    try:
        process = subprocess.run(tokenized_command, capture_output=True, text=True)
        # Parse the JSON output
        data = json.loads(process.stdout)
        # Return the IP address from the JSON data
        return data['ip']

    except json.JSONDecodeError:
        return "Error: Invalid JSON response."
    except Exception as e:
        return f"Error: {e}"



if __name__ == '__main__':
    ip_address = main()
    print(f"Your IP address is: {ip_address}")

