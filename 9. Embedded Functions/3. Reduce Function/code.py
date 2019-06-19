from functools import reduce
def cift(i):
    if(i%2==0):
        return True
    else:
        return False
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(cift,list1))
reduce(lambda x,y:x+y,list2)
