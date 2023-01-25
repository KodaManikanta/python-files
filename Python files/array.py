row=3
colo=2
arr=[]
for i in range(row):
    element=[]
    for j in range (colo):
        element.append(int(input("enter a num:")))
    arr.append(element)
print(arr,end='/')