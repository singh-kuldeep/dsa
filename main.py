num1 = {"a":11}
num2 = num1

print(id(num1))
print(id(num2))

num2['b'] = 32
print(num1, num2)