int = input("Please enter your own int :")

int2 = ('')

for i in int:
    print(i)
    int2 = i + int2
 

print("\n The Original Integer =", int)
print("The Reversed Integer =",int2)

