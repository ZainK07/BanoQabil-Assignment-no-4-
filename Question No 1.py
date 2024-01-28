#Python Program to count unique values inside a list

def a(list):
    b = set()

    for value in list:
        b.add(value)

    return len(b)

list1 = [1,2,3,4,2,3,6,7,8,9,10]
answer = a (list1)
print("Number of unique values:", answer)
