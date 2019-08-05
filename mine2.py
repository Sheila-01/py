#checks type of number
print("Please Enter number:")
num = int (input())
print(type(num))
if(isinstance(num, int)):
    if num % 2 == 0:{
        print("It's an Even Number")}
    else:
        print("It's an Odd Number")
else: 
    print("Please enter an integer")