from pathlib import Path

rotations = Path("input.txt").read_text().splitlines()
password = 0
currentPosition = 50

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:]) % 100
    if direction == "L":
        currentPosition -= distance
        if currentPosition < 0:
            currentPosition += 100
    elif direction == "R":
        currentPosition += distance
    currentPosition = currentPosition % 100
    if currentPosition == 0:
        password += 1

print("Password:", password)