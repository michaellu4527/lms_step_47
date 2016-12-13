"""my_list = ['one', 'two', 'three', 'four', 'five']   # Creating list
my_list_len = len(my_list)  # Getting length of list

for i in range(0, my_list_len):
    print(my_list[i])   # Printing out elements of list
"""

# Drill 1
list1 = [0,1,2,3]
list_len = len(list1)

print("\nDrill 1")
for i in range(0, list_len):
    print("Item ", i, ": ", list1[i])

# Drill 2
print("\nDrill 2")
for i in range(list_len)[::-1]:     # [::-1] indicates to loop in decreasing order
    print("Item ", i, ": ", list1[i])

# Drill 3
list2 = [2,4,6,8]
list_len2 = len(list2)

print("\nDrill 3")
for i in range(list_len2)[::-1]:     # [::-1] indicates to loop in decreasing order
    print("Item ", i, ": ", list2[i])