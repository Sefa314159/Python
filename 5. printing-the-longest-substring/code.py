s = 'abcbcd'
temp = s[0]
long=s[0]

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        temp += s[i+1]
        if len(temp) > len(long):
            long=temp
    else:
        temp=s[i+1]
print(long) 
