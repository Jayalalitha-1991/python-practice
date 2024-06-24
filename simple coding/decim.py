import decimal

a=10

b='1234'

print(decimal.Decimal(a))

print(type(decimal.Decimal(a)))

print(decimal.Decimal(b))

string = 'Python developer'
print("the reverse of the string is:")
# reverse of the string
print(string[::-1])

# counting the vowels on the string

vowels = ['a','e','i','o','u']

count = 0

for character in string:
    if character in vowels:
        count += 1
print("The vowels in string are:",count)

string2 = "This is a sample python programming"
count1=0
for char in string2:
    if char not in vowels:
        count1 +=1
print(count1)

# occurance of a character in string
charcte = 's'
count3 = 0
for letter in string2:
    if letter == charcte:
        count3 +=1
print(count3)