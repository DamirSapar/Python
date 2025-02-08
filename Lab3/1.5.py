from itertools import permutations
def perm(s):
    return sorted(set("".join(p) for p in permutations(s)))

a=input()
print(perm(a))