def pallindome(number):
    number_str=str(number)

    reversed_str=number_str[::-1]

    if reversed_str == number_str:
        return True
    else:
        return False
    

num=int(input("Enter the number"))

if pallindome(num):
    print(True)
else:
    print(False)    
