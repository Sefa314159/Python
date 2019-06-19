list1=[(3,4,5),(6,8,10),(3,10,7)]
def triangle(tup2):
    if(tup2[0]+tup2[1]>tup2[2] and tup2[1]+tup2[2]>tup2[0] and tup2[0]+tup2[2]>tup2[1]):
        return True
    else:
        return False
list(filter(triangle,list1))
