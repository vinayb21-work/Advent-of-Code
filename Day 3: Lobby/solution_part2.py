from pathlib import Path

def maxBattery(batteries):
    res = []
    startIndex = 0
    endIndex = len(batteries) - 12
    while endIndex <= len(batteries):
        maxDigit = max(batteries[startIndex:endIndex+1])
        res.append(maxDigit)
        startIndex = startIndex + batteries[startIndex:endIndex+1].index(maxDigit) + 1
        endIndex = len(batteries) - 12 + len(res)
        if len(res) == 12:
            print("res", res)
            return int("".join(res))

    return res

batteryBanks = Path("input.txt").read_text().splitlines()
maxOutputJoltage = 0
for batteries in batteryBanks:
    maxOutputJoltage += maxBattery(batteries)
print("maxOutputJoltage", maxOutputJoltage)
