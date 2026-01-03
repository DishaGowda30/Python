num = list(map(int, input("Enter the list of numbers: ").split()))
lst=[]
for i in num:
    if i%2==0:
        lst.append(i)
print("The list of even number: ",lst)