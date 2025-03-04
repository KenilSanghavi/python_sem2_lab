import random

odd=[]
while len(odd)<5:
    n=random.randint(1,20)
    if(n%2!=0):
        odd.append(n)
evens=[]
while len(evens)<4:
    n=random.randint(1,20)
    if(n%2==0):
        evens.append(n)
print(evens)
print(odd)
odd.insert(2,evens)
print(odd)
print(evens.sort())
