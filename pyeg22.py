a=int(input("Enter the 1st num:"))
b=int(input("Enter the 2nd num:"))
c=int(input("Enter the 3rd num:"))
if a>b:
    if a>c:
        print(f"The largest number is:{a}")
    else:
        print(f"The largest number is:{c}")
else:
    if b>c:
        print(f"The largest number is:{b}")
    else:
        print(f"The largest number is:{c}")
