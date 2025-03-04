import random
positive=[]
negative=[]
for i in range(30):
    n=random.randint(-100,100)
    if(n<0):
        negative.append(n)
    else:
        positive.append(n)
print(positive,negative,len(positive),len(negative))
