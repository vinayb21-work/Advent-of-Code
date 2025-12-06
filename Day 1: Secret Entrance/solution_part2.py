from pathlib import Path

rotations = Path("input.txt").read_text().splitlines()
password = 0
currentPosition = 50

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    
    # Count full rotations (each passes through 0 once)
    if distance >= 100:
        password += distance // 100
    distance = distance % 100
    
    if direction == "L":
        # Going left: we pass 0 if we start above 0 and move far enough to reach/cross it
        if currentPosition > 0 and distance >= currentPosition:
            password += 1
        currentPosition -= distance
        if currentPosition < 0:
            currentPosition += 100
    elif direction == "R":
        # Going right: we pass 0 if we wrap around (position + distance >= 100)
        if currentPosition + distance >= 100:
            password += 1
        currentPosition = (currentPosition + distance) % 100

print("Password:", password)