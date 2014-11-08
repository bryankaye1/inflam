
def assign_drug(dataname): 
    number = dataname[13:-4]
    result = 'Nope'
    if (int(number) % 2) == 0: 
        result = "tylenol"
    elif (int(number) % 2) == 1: 
        result = "placebo"
    else:
        result= "neither even nor odd"
    return result

import sys

filename = sys.argv[1]
print assign_drug(filename)

assert assign_drug("inflammation_0.dat") == "tylenol"
assert assign_drug("inflammation_1.dat") == "placebo"
assert assign_drug("inflammation_2.dat") == "tylenol"
