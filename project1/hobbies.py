# def count():
    # print(__name__)

#count()
likes = ["no-hobbies", "dancing", "eating", "playing"]
for like in likes:                                                           # "for" and "in" on the same line help to loop
    print(like)

myVar = "m" in "emma"                                                        #"in" here helps to check
print(myVar)                                                                 #prints a boolean value "true" after the check

name = "Lynne"
for position in range(len(name)):                                            #
    print(name[position])                                                    #

for number in range(6):                                                     #A loop to print numbers in that range
    print(number)

for letter in "sheilla":
    # print(letter)
    print("sheilla".count("l"))                                            #the count method to count 'l'

name = "Sheene"
for item, post in enumerate(name):
    print(item,post)
print("**********")

for number in range(2,10):
    if number % 2 == 0:
        print(number, "is even")
    continue
