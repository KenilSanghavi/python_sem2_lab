x=int(input("Enter x : "))
y=int(input("Enter y : "))
h=int(input("Enter h : "))
k=int(input("Enter k : "))
r=int(input("Enter radius : "))
ans=((x-h)**2)+((y-k))**2-(r**2)
if ans<0:
    print("Given poins lies inside the circle")
elif ans==0:
    print("Given poins lies on the circle")
else:
    print("Given poins lies outside the circle")
