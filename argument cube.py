def cube(num):
    return num * num * num

num = 10
print(f"The Cube of {num} is {cube(num)}")

def by_three(number):
    if (num %3) == 0:
        return cube(number)
    else: return False

print(by_three(14))
print(by_three(20))
print(by_three(15))