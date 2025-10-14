# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres 
# of water per hour of cycling.
# You get given the time in hours and you need to return the 
# number of litres Nathan will drink, rounded down.

#definetly should just import math :) 
#0.5*hr
def litres(time):
    vol = 0.5*time
    vol = vol - (vol %1)
    return round(vol)

    #return time //2 # like are you serious?? am i stupid
print(litres(6.7))
