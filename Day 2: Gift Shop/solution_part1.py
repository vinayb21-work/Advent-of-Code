from pathlib import Path

def isValidId(id):
    if len(id) % 2 != 0:
        return True

    return id[:len(id) // 2] * 2 != id 

idRanges = Path("input.txt").read_text().split(",")
invalidIds = []
for idRange in idRanges:
    start, end = idRange.split("-")
    # print("start", start, "end", end)
    for id in range(int(start), int(end) + 1):
        if not isValidId(str(id)):
            # print("adding id", id)
            invalidIds.append(id)

# print(invalidIds)
print("sum", sum(invalidIds))
# print(sum(invalidIds))


