from pathlib import Path

batteryBanks = Path("input.txt").read_text().splitlines()
maxOutputJoltage = 0
for batteries in batteryBanks:
    # print("batteries", batteries)
    currentMaxJoltage = 0
    i = 0
    j = 1
    while j < len(batteries):
        voltage = int(batteries[i] + batteries[j])
        currentMaxJoltage = max(currentMaxJoltage, voltage)
        if batteries[j] > batteries[i]:
            i = j
        j += 1
    # print("currentMaxJoltage", currentMaxJoltage)
    maxOutputJoltage += currentMaxJoltage
print("maxOutputJoltage", maxOutputJoltage)
