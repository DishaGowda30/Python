my_list=[1,2,3,4,1,2,3,1,6,7,8,9,1,3]
unique_numbers = []
for i in my_list:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(unique_numbers)