terms=int(input("Enter how many terms:"))
result = list(map(lambda x: 2 ** x, range(terms)))
print(result)