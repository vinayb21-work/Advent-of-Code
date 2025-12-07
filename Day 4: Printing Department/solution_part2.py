from pathlib import Path

paperRollChar = "@"

def isAccessible(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            adjacentNeighbourCount = 0
            if grid[row][column] == paperRollChar:
                if row > 0 and column > 0:
                    if grid[row-1][column-1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if row < len(grid) - 1:
                    if grid[row+1][column] == paperRollChar:
                        adjacentNeighbourCount += 1
                    if column < len(grid[row]) - 1:
                        if grid[row+1][column+1] == paperRollChar:
                            adjacentNeighbourCount += 1
                    if column > 0:
                        if grid[row+1][column-1] == paperRollChar:
                            adjacentNeighbourCount += 1
                if column > 0:
                    if grid[row][column-1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if row > 0:
                    if grid[row-1][column] == paperRollChar:
                        adjacentNeighbourCount += 1
                    if column < len(grid[row])-1 and grid[row-1][column+1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if column < len(grid[row]) - 1:
                    if grid[row][column+1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if adjacentNeighbourCount < 4:
                    return True
    return False

paperRolls = Path("input.txt").read_text().splitlines()
rows = len(paperRolls)
grid = []
for row in paperRolls:
    grid.append(list(row))
accessiblePaperRolls = 0
accessible = True

while accessible:
    # print("grid", grid)
    accessibleCells = set()
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            adjacentNeighbourCount = 0
            if grid[row][column] == paperRollChar:
                if row > 0 and column > 0:
                    if grid[row-1][column-1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if row < len(grid) - 1:
                    if grid[row+1][column] == paperRollChar:
                        adjacentNeighbourCount += 1
                    if column < len(grid[row]) - 1:
                        if grid[row+1][column+1] == paperRollChar:
                            adjacentNeighbourCount += 1
                    if column > 0:
                        if grid[row+1][column-1] == paperRollChar:
                            adjacentNeighbourCount += 1
                if column > 0:
                    if grid[row][column-1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if row > 0:
                    if grid[row-1][column] == paperRollChar:
                        adjacentNeighbourCount += 1
                    if column < len(grid[row])-1 and grid[row-1][column+1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if column < len(grid[row]) - 1:
                    if grid[row][column+1] == paperRollChar:
                        adjacentNeighbourCount += 1
                if adjacentNeighbourCount < 4:
                    accessibleCells.add((row, column))
                    accessiblePaperRolls += 1
    for row, column in accessibleCells:
        grid[row][column] = "."
    accessible = isAccessible(grid)
print("accessiblePaperRolls", accessiblePaperRolls)    