# #multiplying list
numbers = [60, 20, 30, 50,40,70,45,57,96]
num = 1
for i in numbers:
   num *= i
print("Product of elements in the list:", num)

numbers1 = sorted(numbers)
# print(type(numbers1))
print(numbers[-5:-8:-1])#reversed slicing
#(start:end:steps)
# print(numbers1[0])
# print(type(numbers1[0]))
# print(numbers1[4])
print((numbers))
minimum = numbers[0]
# for i in numbers:
#     if i<minimum:
#         minimum=i
#         print(minimum)

for i in numbers:
    if i > minimum:
      minimum = i
# Print the minimum value
# print("The largest number in the list is:", minimum)

a = [2,4,5,6,1,9,8,7]
b = sorted(a)
print(b)
if len(b)>=2:
    print(b[1])

c =[num for num in b if num%2==0 ] #even numbersi in list
print(c)
d=[nums for nums in b if nums%2!=0]#odd numbers in list
print(d)

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filter =[i for i in list_of_lists if i]#filtering list
print(filter)

#cloning the list
original_list = [1, 2, 3, 4, 5]
clone = original_list[:]
print(clone)

#Split a string into a list of words
string = "Split a string into a list of words"
str=string.split()
print(str)

# strig = seperator.str.join()
# print(strig)


#unique value from dictionary
my_dict = {
'a': 10,
'b': 20,
'c': 10,
'd': 30,
'e': 20
}

# uni_val = set()
# for i in my_dict.values():
#     uni_val.add(i)
#     uni_val_list=list(uni_val)
#     print(uni_val_list)

#add values in dictionary
total_sum = 0
# Iterate through the values of the dictionary and add them to the tota
for i in my_dict.values():
    total_sum += i
# Print the sum of all items in the dictionary
print(total_sum)

#merge two dic
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)