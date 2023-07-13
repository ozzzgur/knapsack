#import numpy as np
from itertools import product


###Solving a Knapsack Problem with List Compherensions

#Weights of objects
weights = [30,10,40,20]

#Values of objects
values = [10,20,30,40]

#We need a solution space for the problem,therefore we create space list.

space=[]
#Solution_space function creates a solution space for the problem, and assign it to space list


def solution_space(w,p):

    numerator =list(product([0,1],repeat=len(weights)))
    for i,j,k,v in numerator:
        total_w = 0
        total_p= 0
        total_w = weights[0] * i + weights[1] * j + weights[2] * k + weights[3] * v
        total_p = values[0] * i + values[1] * j + values[2] * k + values[3] * v
        space.append([total_w,total_p])
    return space


solution_space(weights,values)


#best_solution function determines the weight constrain in the problem and
#Finally result of the solution


def best_solution(space,limit=0):
    numerator = list(product([0, 1], repeat=len(weights)))
    last = [[i, j] for i, j in space if i <= limit]
    solo =[]
    for i,j in last:
        solo.append(j)
        solu=max(solo)
    for i,j in last:
        if j== solu:
            final=[i,j]
    indx=space.index(final)
    print("1-0 s indicate which object was selected")
    print(numerator[indx])
    print("Best result is "+str(solu))


best_solution(space,40)


