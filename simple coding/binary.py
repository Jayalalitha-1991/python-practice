def is_binary(number):
    for digit in number:
        if digit  not in ['0','1']:
            return False
        return True
    
num= input("ENter the nuber: ")

if is_binary(num):
    print("True")

else:
    print("False")