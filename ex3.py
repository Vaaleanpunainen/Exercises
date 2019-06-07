import itertools

n = input("Enter a number from 0-10000: ")

def permut(n):
    return [int("".join(n)) for n in itertools.permutations(n)]

def find_max(n):
    return int("".join(sorted(str(n), reverse=True)))

print(permut(n))
print(find_max(n))
