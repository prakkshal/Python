def find():
    a=int(input("Enter the length:"))
    b=int(input("Enter the breadth:"))
    area=a*b
    p=2*(a+b)
    
    if area>p:
      print("the area of rect is greater")
    else:
     print("the area of rect is not greater")
find()
