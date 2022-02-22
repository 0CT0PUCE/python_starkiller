import random

n = random.randint(1,4)
print(n)
global d
d=0
def ran():
    global d
    n = random.randint(1,4)
    if n==1 :
        d=1
    if n == 2 :
        d=2
    if n == 3 :
        d=3
    if n == 4 :
        d=4

ran()

print(d)
