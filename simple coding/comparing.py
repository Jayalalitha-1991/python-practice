string1 = 'one'
string2 ='two'

string1 = list(string1.upper())

string2 = list(string2.upper())

string1.sort() 
string2.sort()

if (string1==string2):
    print("The both strings are matched")

else:
    print("The both strings are not matched")

