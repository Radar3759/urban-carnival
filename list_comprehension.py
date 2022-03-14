# multiply each number by 2
nums = [4, 8, 15, 16, 23, 42]
double_nums = [num*2 for num in nums]
# long version commented out below
# for num in nums:
#   double_nums.append(num * 2)
print(double_nums)

# Squares
# range from 1-10
nums = range(11)
# make a new, empty list named 'squares'
squares = [num ** 2 for num in nums]
# #iterate through each item in list nums
# for num in nums:
#   #make each item squared
#   squares.append(num **2)
# print the list of squares
print(squares)

# Add 10
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]

print(add_ten)

# Div by 2
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num // 2 for num in nums]
# long version
# for num in nums:
#   (divide_by_two.append(num // 2))
print(divide_by_two)
#Even or odd
nums = [4, 8, 15, 16, 23, 42]
# modulo will eval to 0 for even, 1 for odd
parity = [num % 2 for num in nums]
print(parity)

#Add Hello
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]

#First Char
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
# for name in names:
#   first_character.append(name[0])
print(first_character)

#length
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [ len(name) for name in names]
print(lengths)

#opposite
booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]
