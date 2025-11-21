square=lambda s:s*s
rectangle=lambda l,b:l*b
triangle=lambda b,h:0.5*b*h
s=float(input("enter side of square:"))
l=float(input("enter length of rectange:"))
b=float(input("enter breadth of rectange:"))
tb=float(input("enter base of triangle:"))
h=float(input("enter height of triangle:"))
print("Area of square:",square(s))
print("Area of rectangle:",rectangle(l,b))
print("Area of triangle:",triangle(tb,h))
