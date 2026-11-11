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

def proper_factors(n):
    if n == 0:
         return []
    else:
        return [i for i in range(2, n ) if n % i == 0]


repeat=[]
for i in ranges1:
    for ID in range(i[0], i[1]+1):
        for k in proper_factors(len(str(ID))):
            if len(str(ID))%k == 0:
                if all(str(ID)[j] == str(ID)[j+(len(str(ID))//k)] for j in range(len(str(ID))-(len(str(ID))//k))):
                    repeat.append(ID)
                    break
print(sum(repeat))