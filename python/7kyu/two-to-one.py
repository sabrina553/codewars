'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
'''
def longest(a,b):
    return ''.join(sorted(set(a+b)))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) # -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
