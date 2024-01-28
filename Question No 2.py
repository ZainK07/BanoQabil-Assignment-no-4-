# write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

def generate_square_dictionary(n):
    square_dict = {i: i*i for i in range(1, n+1)}
    return square_dict

# Example usage with n = 5
n = 5
result_dict = generate_square_dictionary(n)
print(result_dict)
