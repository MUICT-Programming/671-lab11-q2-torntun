# YOUR CODE HERE
lst1 = []
lst2 = []
updated_list = []
num = int(input())
for i in range (num):
    lst1.append(int(input()))
for i in range (num):
    lst2.append(int(input()))

def sumation(lst1,lst2):
    for i in range(len(lst1)):
        total = 0
        total += lst1[i] + lst2[i]
        updated_list.append(total)
    return updated_list

def find_min_max(updated_list):
    tup = ()
    tuplist = []
    first = updated_list[0]
    last = 0
    for i in updated_list:
        if i < first:
            first = i
    tuplist.append(first)
    for i in updated_list:
        if i > last :
            last = i
    tuplist.append(last)
    tup = tuple(tuplist)
    return tup

print(sumation(lst1,lst2))
print(find_min_max(updated_list))
