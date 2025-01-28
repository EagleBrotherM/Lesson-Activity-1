string = input("Please enter your own word")

char = input("Please enter your own Character")

i = 1
count = 0

for i in range (len(string)):

    if (string [i] == char):
        count = count + 1
    i = i + 1

print("The Total Number of Times ", char, "Has Occured = " , count) 