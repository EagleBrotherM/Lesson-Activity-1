string = input("Please enter your own string :")

string2 = ('')

for i in string:
    print(i)
    string2 = i + string2
 

print("\n The Original String =", string)
print("The Reversed String =",string2)

