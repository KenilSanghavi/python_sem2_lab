import random
li=[]
x=int(input("Enter number : "))
for i in range(20):
    n=random.randint(1,3)
    li.append(n)
    if(n==x):
        print("Found at index : ",i)
