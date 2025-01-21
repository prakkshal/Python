def line():
    if (y2-y1)/(x2-x1)==(y3-y2)/(x3-x2):
        print("all points are on line")
    else:
        print("all points are not on line")
x1=int(input("x coordinate of 1st point:"))
y1=int(input("y coordinate of 1st point:"))
x2=int(input("x coordinate of 1st point:"))
y2=int(input("y coordinate of 1st point:"))
x3=int(input("x coordinate of 1st point:"))
y3=int(input("y coordinate of 1st point:"))
line()
