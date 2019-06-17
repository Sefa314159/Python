def gcd(r,t):
    list1 = []
    list2 = []
    for i in range(2,r+1):
        if(r%i==0):
            list1.append(i)
    for j in range(2,t+1):
        if(t%j==0):
            list2.append(j)
    for x in range(len(list1) - 1, -1, -1):
        for y in range(len(list2) - 1, -1, -1):
            if (list2[y] == list1[x]):
                print("Greatest Commoon Divisor is", list2[y])
                break
        if (list2[y] == list1[x]):
            break
    print("Divisors of {} are {}".format(r, list1))
    print("Divisors of {} are {}".format(t, list2))

while True:
    a=input("Enter the first number:")
    if(a=="q"):
        print ("Closing app...")
        break
    else:
        a=int(a)
        if(a==0 or a==1):
            print ("you can't write",a)
        b=input("Enter the second number")
        if(b=="q"):
            print ("Closing app...")
            break
        else:
            b=int(b)
            if(b==0 or b==1):
                print ("you can't write",b)
            else:
                gcd(a,b)
