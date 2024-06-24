String = input('Enter the string :')
#take character input
Character = input('Enter character :')
#initiaalize int variable to store frequency
frequency = 0
#use count function to count frequency of character
frequency = String.count(Character)
#count function is case sencetive 
#so it print frequency of Character according to given Character
print(str(frequency) + ' is the frequency of given character')