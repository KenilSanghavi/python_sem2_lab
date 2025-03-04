import random
l=[]
dup=[]
for i in range(50):
    n=random.randint(1,30)
    l.append(n)
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)
