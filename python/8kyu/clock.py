def ms(s):
    return 1000*s
def past(h, m, s):
    time = 0
    time += ms(s)
    time += ms(m*60)
    time += ms(h*60**2)
    return time
    
## why did i do it this way :/ (note to self, 8kyu really can be done in 
## one return but nice try anyway :)
def bestpast(h, m, s):
    return (3600*h + 60*m + s) *1000

print(past(1,1,1))
