def filter_list(l):
    a=[]
    for i in l:
        if type(i) == int:
            a.append(i)
    return a
#seemingly works atp -- passes all tests 

def better(l):
    ## if returning as a list, can be embedded in []
    return [x for x in l if type(x) is not str]
    #alternatively 
    #return [i for i in l if not isinstance(i, str)]
print(filter_list([1,2,'a','b',0,15]))
print(better([1,2,'a','b',0,15]))
