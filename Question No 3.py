# Python program to display the sum of n numbers using a list

def sum_of_numbers(numbers):
    return sum(numbers)


user_numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
result = sum_of_numbers(user_numbers)
print(f"The sum of the numbers is: {result}")
