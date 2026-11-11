from pathlib import Path

data=""
with open(Path(__file__).with_name("input.txt")) as f:
    data = f.read()

if len(data) < 1:
    with open(Path(__file__).with_name("test.txt")) as f:
        data = f.read()

ranges=data.split(",")
ranges1 = []

for i in ranges:
    min_range, max_range = i.split("-")
    ranges1.append((int(min_range), int(max_range)))


repeat=[]
for i in ranges1:
    for j in range(i[0], i[1]+1):
        if len(str(j))%2 == 0:
            if all(str(j)[k] == str(j)[k+((len(str(j)))// 2)] for k in range((len(str(j)))// 2)):
                repeat.append(j)
print(sum(repeat))