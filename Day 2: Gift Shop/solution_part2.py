from pathlib import Path

def isValidId(id):
    n = len(id)
    for i in range(1, n // 2 + 1):
        if id[:i] * (n // i) == id:
            return False
    return True

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
