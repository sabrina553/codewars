# your classmate asks you to copy paperwork 
# there are n class mates and m pages per item
# calculate how many blank pages do you need, if n,m < 0 return 0 
#second attempt
def paperwork(n, m):
    return n*m if all(i > 0 for i in [n,m]) else 0

#doesn't work for double negatives :? first attempt]
def paperwork2(n, m):
    return n*m if n*m > 0 else 0

def paperworkbestprac(n,m):
    return n*m if n> 0 and m > 0 else 0
print(paperwork(3,-3))
