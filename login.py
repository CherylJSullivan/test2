import pyautogui
import subprocess
import time
import os

# Define the duration between each action (in seconds)
duration = 5

# Read the secrets from the file
secrets = {}
with open("secrets.txt") as file:
    for line in file:
        key, value = line.strip().split("=")
        secrets[key] = value

# Define the coordinates and use the secrets
actions = [
    ((681, 530), None),  # install
    ((506, 499), None),
    ((154, 379), None),  # device
    ((154, 379), None),  # device
    ((331, 282), None),  # Log in
    ((458, 333), secrets["EMAIL_SECRET"]), # email (type email secret from env after clicking)
    ((449, 375), secrets["PASSWORD_SECRET"]), # pass (type password secret from env after clicking)
    ((518, 435), None)  # log in
]

# Function to perform the taskkill operation with retries
def taskkill_process(process_name, max_retries=5, retry_delay=5):
    for _ in range(max_retries):
        try:
            subprocess.run(["taskkill", "/f", "/im", process_name])
            return True  # Return True if the taskkill is successful
        except subprocess.CalledProcessError:
            print(f"Failed to kill {process_name}. Retrying in {retry_delay} seconds.")
            time.sleep(retry_delay)
    return False  # Return False if the taskkill failed even after the maximum retries

# Wait for a few seconds to give time to focus on the target application
time.sleep(5)

# Iterate through the actions and perform each one
for pos, text in actions:
    pyautogui.click(pos)
    if text is not None:
        pyautogui.typewrite(text)
    time.sleep(duration)  # Wait for the specified duration before proceeding to the next action

    # Check if the current action is to close Microsoft Edge
    if pos == (506, 499):
        # Execute the "taskkill" command to close Microsoft Edge with retries
        if taskkill_process("msedge.exe"):
            # If at least one process was successfully closed, continue the script
            continue
        else:
            # If taskkill fails for all retries, exit the script or handle the error as needed
            print("Failed to close Microsoft Edge. Exiting the script.")
            sys.exit(1)  # Exit the script with an error code

# Additional actions here if needed
