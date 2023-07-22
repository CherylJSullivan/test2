import pyautogui
import subprocess
import time
import os

# Define the duration between each action (in seconds)
duration = 5

# Define the coordinates and environment variable keys to get values for email and password
actions = [
    ((681, 530), None),  # install
    ((506, 499), None),
    ((154, 379), None),  # device
    ((331, 282), None),  # Log in
    ((458, 333), os.getenv("EMAIL_SECRET")), # email (type email secret from env after clicking)
    ((449, 375), os.getenv("PASSWORD_SECRET")), # pass (type password secret from env after clicking)
    ((518, 435), None)  # log in
]

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
        # Execute the "taskkill" command to close Microsoft Edge
        subprocess.run(["taskkill", "/f", "/im", "MicrosoftEdge.exe"])
