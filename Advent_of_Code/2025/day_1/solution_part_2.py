from pathlib import Path


start=50
data=[]

with open(Path(__file__).with_name("input.txt")) as f:
    data = f.read()

if len(data) < 1:
    with open(Path(__file__).with_name("test.txt")) as f:
        data = f.read()

commands=data.split()


c=0
prev=50
for i in commands:

    if i[0] == "L":
        start -= int(i[1:])
    elif i[0] == "R":
        start += int(i[1:])


    if start <=0 :
        if prev == 0 :
            c -= 1
        elif start%100 == 0:
            c+=1

    c+=abs(start//100)
    start = start%100

    prev = start

    

print(c)