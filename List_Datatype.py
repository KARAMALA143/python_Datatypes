my_list = [1,2,3,4]
print("Initial list:",my_list)

my_list.append('Python')
print("After performing append():",my_list)

my_list.insert(2,'DBMS')
print("USage of insert method:",my_list)

print("Adding new piece of code for the project which cloned from my own remote repo")
my_list.append('100')
print(my_list)

print("Find the missing numbers in the given list")
my_list = [1,4,2,5,6,8]
min_num = min(my_list)
max_num = max(my_list)
missing_num = []
for num in range(min_num,max_num+1):
    if num not in my_list:
        missing_num.append(num)
print("Missing number or numbers: ", missing_num)