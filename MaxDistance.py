#We will use the itertools library in order to make tuples in sorted order with no repeated elements later in the code.
import itertools

def maxDistance(numbers, limit):
    sumNum = 0
    for N in range(0, len(numbers) + 1):
        for dsets in itertools.combinations(numbers, N): #Here appears the reason we imported the itertools library.
            s = sum(dsets)
            if s > sumNum and s <= limit:
                sumNum = s
    print("The closest sum of the list's numbers to : " , limit, " is: ", sumNum)

#Default example:
maxDistance([16, 35, 53], 79)



#python 2.x and 3.x compatible