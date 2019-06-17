def perfect(x):
    list1 = []
    j = 0
    sum=0
    for i in range(1,x):
        if(x%i==0):
            list1.append(i)
            j+=1
    for k in range(0,j):
        sum+=list1[k]
    if(x==sum):
        return True
    else:
        return False

while True:
    value=input("Enter an integer(press 'q' if you want to quit):")
    if(value=="q"):
        break
    value=int(value)
    if(perfect(value)):
        print ("{} is a Perfect Number.".format(value))
    else:
        print ("{} is not a Perfect Number.".format(value))
