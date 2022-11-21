#(0,0) (0,5) (7,0) üçgen kordinatları

def find_coordinates(x,y):
    if x == 0 and y <= 5:
        print("True")
    elif x<= 7 and y==0:
        print("True")
    elif 7 >= x > 0  and 5 >= y > 0:
        print("True")
    else:
        print("False")

find_coordinates(0,2)
