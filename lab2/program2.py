a,b,c=10,20,30
if a>b and a>c:
    print("a is the largest")
    if b>c:
        print("c is the smallest")
    else:
        print("b is the smallest")
elif b>a and b>c:
    print("b is the largest")
    if a>c:
        print("a is the smallest")
    else:
        print("c is the smallest")
else:
    print("c is the largest")
    if a>b:
        print("cbis the smallest")
    else:
        print("a is the smallest")
