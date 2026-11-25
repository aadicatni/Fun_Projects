from pathlib import Path

data=""
# with open(Path(__file__).with_name("input.txt")) as f:
#     data = f.read()

if len(data) < 1:
    with open(Path(__file__).with_name("example.txt")) as f:
        data = f.read()

data=[list(i) for i in data.strip().splitlines()]
neighbors=[[0 for j in i] for i in data]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="@":
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0<=i+x<len(data) and 0<=j+y<len(data[i]):
                        if not (x==0 and y==0):
                            neighbors[i+x][j+y] += 1

total=0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="@" and neighbors[i][j] < 4:
            total += 1

print(total)