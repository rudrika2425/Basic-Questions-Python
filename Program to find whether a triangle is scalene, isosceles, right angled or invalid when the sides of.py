a=eval(input())
b=eval(input())
c=eval(input())
if(a+b>c or a+c>b or b+c>a):
    if(a!=b!=c):
        print("triangle is scalene")
    elif(a==b==c):
        print("triangle is equilateral")
    else:
        print("triangle is isoceles")
else:
    print("triangle is invalid")
