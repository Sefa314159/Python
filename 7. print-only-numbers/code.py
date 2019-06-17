list = ["345", "sadas", "324a", "14", "kemal"]
temp = []
for i in range(0, len(list) - 1):
    try:
        list[i]=int(list[i])
        temp.append(list[i])
    except ValueError:
        continue
print(temp)
