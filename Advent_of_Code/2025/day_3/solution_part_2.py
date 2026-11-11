from pathlib import Path

data=""
with open(Path(__file__).with_name("input.txt")) as f:
    data = f.read()

if len(data) < 1:
    with open(Path(__file__).with_name("test.txt")) as f:
        data = f.read()

banks=data.split()
max_joltages=[]
selected=12

for bank in banks:
    joltages=[int(i) for i in bank]
    digits=[max(joltages[:-selected+1])]
    for i in range(1,selected):
        joltages=joltages[joltages.index(digits[-1])+1:]
        digits.append(max(joltages[:len(joltages)-selected+i+1]))
        # print(digits, joltages,bank,joltages[:len(joltages)-selected+i+1])

    max_joltages.append(sum(digits[i] * 10**(selected-i-1) for i in range(len(digits))))
print(sum(max_joltages))
# print(max_joltages)