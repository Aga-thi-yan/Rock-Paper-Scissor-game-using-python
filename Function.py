# Function

def Agathiyan():
    print("hi")


Agathiyan()

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return  "pls enter integer value"
    return num1 + num2

total = sum(54978,54)

print(total)


def multiple_numbers (*args):
    print(args)
    print(type(args))

multiple_numbers ("agatghiyan","25")

def add(*num):
    sum =0
    for n in num:
        sum= sum+n
    print(sum)    

add (545721,6566) 

