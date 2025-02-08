def uniq(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

d = ["Cucumber", "Apple", "Strawberry", "Banana", "Apple"]
print(uniq(d))
