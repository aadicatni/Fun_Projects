from pathlib import Path

data=""
with open(Path(__file__).with_name("input.txt")) as f:
    data = f.read()

if len(data) < 1:
    with open(Path(__file__).with_name("test.txt")) as f:
        data = f.read()

banks=data.split()
max_joltages=[]
for bank in banks:
    joltages=[int(i) for i in bank]
    first_digit=max(joltages[:-1])
    second_digit=max(joltages[joltages.index(first_digit)+1: ])
    max_joltages.append((first_digit*10 + second_digit))

print(sum(max_joltages))
# print(max_joltages)