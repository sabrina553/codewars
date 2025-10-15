'''
Given a string of words return the length of the shortest word(s)

emphaises on (s)
'''
def find_short(s):
    a = s.split()
    c = 1000000
    for i in a:
        length = len(i)
        if length < c:
            c = length
    return c

'''
i feel like I'm approaching python like it's a real langauge
so many embeded functions
'''
def simple(s):
    s = s.split() # splits list into individual, don't need to create a new variable for this :/
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) ## which can be further simplified
def best(s):
    return min(len(x) for x in s.split())
print(find_short("bitcoin take over the world maybe who knows perhaps"))
