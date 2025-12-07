from pathlib import Path

paperRolls = Path("input.txt").read_text().splitlines()
rows = len(paperRolls)
grid = []
for row in paperRolls:
    grid.append(list(row))
accessiblePaperRolls = 0
paperRollChar = "@"
# print(grid)
for row in range(len(grid)):
    for column in range(len(grid[row])):
        adjacentNeighbourCount = 0
        if grid[row][column] == paperRollChar:
            # print("================================")
            if row > 0 and column > 0:
                if grid[row-1][column-1] == paperRollChar:
                    # print("top left")
                    adjacentNeighbourCount += 1
            if row < len(grid) - 1:
                if grid[row+1][column] == paperRollChar:
                    # print("bottom")
                    adjacentNeighbourCount += 1
                if column < len(grid[row]) - 1:
                    if grid[row+1][column+1] == paperRollChar:
                        # print("bottom right")
                        adjacentNeighbourCount += 1
                if column > 0:
                    if grid[row+1][column-1] == paperRollChar:
                        # print("bottom left")
                        adjacentNeighbourCount += 1
            if column > 0:
                if grid[row][column-1] == paperRollChar:
                    # print("left")
                    adjacentNeighbourCount += 1
            if row > 0:
                if grid[row-1][column] == paperRollChar:
                    # print("top")
                    adjacentNeighbourCount += 1
                if column < len(grid[row])-1 and grid[row-1][column+1] == paperRollChar:
                    # print("top right")
                    adjacentNeighbourCount += 1
            if column < len(grid[row]) - 1:
                if grid[row][column+1] == paperRollChar:
                    # print("right")
                    adjacentNeighbourCount += 1
            if adjacentNeighbourCount < 4:
                # print("adjacentNeighbourCount", adjacentNeighbourCount, "row", row, "column", column)
                accessiblePaperRolls += 1
print("accessiblePaperRolls", accessiblePaperRolls)
