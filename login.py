import subprocess
import pyautogui
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

# Wait for a few seconds to give time to focus on the target application
time.sleep(5)

# Iterate through the actions and perform each one
for pos, text in actions:
    pyautogui.click(pos)
    if text is not None:
        pyautogui.typewrite(text)
    time.sleep(duration)  # Wait for the specified duration before proceeding to the next action

    # Check if the current action is to add a 10-second delay after coordinate (506, 499)
    if pos == (506, 499):
        time.sleep(10)

# Execute the "taskkill" command to close Microsoft Edge
subprocess.run(["taskkill", "/f", "/im", "msedge.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ASCII art and echo messages
print("\n..........................................................")
print(".....Brought To You BY ...................................")
print("..........................................................")
print("......#####...######...####....####...##.......####.......")
print("......##..##....##....##......##..##..##......##..##......")
print("......##..##....##.....####...######..##......######......")
print("......##..##....##........##..##..##..##......##..##......")
print("......#####...######...####...##..##..######..##..##......")
print("..........................................................")
print("..Youtube Video Tutorial - https://youtu.be/xHr0cPjSRFg ..")
print("..........................................................")
print("You Can Now Log in to RDP Via AnyViewer")
