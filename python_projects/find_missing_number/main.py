def findNumber(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
lisf_of_numbers = [1,2,3,9,12,17,13,14,15,16,10,11]
print(findNumber(lisf_of_numbers))
