# Day 1: Secret Entrance

## Solution

### Part 1

- Initialise currentPosition at 50 and password to 0
- Iterate through the rotations 
- Parse out the direction and distance from rotation
- Set distance to distance % 100 because one complete rotation in either direction would bring you back to the same position
- Subtract distance from currentPosition when direction is L and if currentPosition becomes negative then add 100 as it's similar to going through an array from right to left and if value becomes negative then you go from last index in right to left direction and dial is a circle
- Similarly when direction is R, add the distance to the currentPosition, no negative currentPosition needs to be handled for this as it's pure addition in positive direction
- Set currentPosition to currentPosition % 100 to avoid any overflow. Ex: currentPosition: 55 and R50 would set currentPosition value to 105 while in actual dial it would be 5 so 105 % 100 == 5 provides us the correct value
- If currentPosition is 0, then increment password by 1
- Print password after iterating through all rotations

### Part 2

- Initialise currentPosition at 50 and password to 0
- Iterate through the rotations
- Parse out the direction and distance from rotation
- Handle full rotations first: if distance >= 100, add distance // 100 to password (each complete rotation passes through 0 once)
- Set distance to distance % 100 to get remaining clicks after full rotations
- For direction L (left):
  - We pass through 0 if we start above 0 AND move far enough to reach/cross it: if currentPosition > 0 and distance >= currentPosition, increment password by 1
  - Subtract distance from currentPosition, if negative add 100 to wrap around
- For direction R (right):
  - We pass through 0 if we wrap around: if currentPosition + distance >= 100, increment password by 1
  - Set currentPosition to (currentPosition + distance) % 100
- Print password after iterating through all rotations

### How to run the solution?

- For part 1
```
python solution_part1.py
```

- For part 2
```
python solution_part2.py
```
