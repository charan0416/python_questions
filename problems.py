# # #multiplying list
# numbers = [60, 20, 30, 50,40,70,45,57,96]
# num = 1
# for i in numbers:
#    num *= i
# print("Product of elements in the list:", num)
#
# numbers1 = sorted(numbers)
# # print(type(numbers1))
# print(numbers[-5:-8:-1])#reversed slicing
# #(start:end:steps)
# # print(numbers1[0])
# # print(type(numbers1[0]))
# # print(numbers1[4])
# print((numbers))
# minimum = numbers[0]
# # for i in numbers:
# #     if i<minimum:
# #         minimum=i
# #         print(minimum)
#
# for i in numbers:
#     if i > minimum:
#       minimum = i
# # Print the minimum value
# # print("The largest number in the list is:", minimum)
#
# a = [2,4,5,6,1,9,8,7]
# b = sorted(a)
# print(b)
# if len(b)>=2:
#     print(b[1])
#
# c =[num for num in b if num%2==0 ] #even numbersi in list
# print(c)
# d=[nums for nums in b if nums%2!=0]#odd numbers in list
# print(d)
#
# list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
# filter =[i for i in list_of_lists if i]#filtering list
# print(filter)
#
# #cloning the list
# original_list = [1, 2, 3, 4, 5]
# clone = original_list[:]
# print(clone)
#
# #Split a string into a list of words
# # Split a string into a list of words
# input_str = "Python program to split and join a string"
# word_list = input_str.split() # By default, split on whitespace
# # Join the list of words into a string
# separator = " " # specify the separator between words
# output_str = separator.join(word_list)
# # Print the results
# print("Original String:", input_str)
# print("List of split Words:", word_list)
# print("Joined String:", output_str)
#
# #unique value from dictionary
# my_dict = {
# 'a': 10,
# 'b': 20,
# 'c': 10,
# 'd': 30,
# 'e': 20
# }
#
# # uni_val = set()
# # for i in my_dict.values():
# #     uni_val.add(i)
# #     uni_val_list=list(uni_val)
# #     print(uni_val_list)
#
# #add values in dictionary
# total_sum = 0
# # Iterate through the values of the dictionary and add them to the tota
# for i in my_dict.values():
#     total_sum += i
# # Print the sum of all items in the dictionary
# print(total_sum)
#
# #merge two dic
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)
# # convert key-values list to flat dictionary.
# key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# flat_dict = {}
# for key,value in key_values_list:
#     flat_dict[key]= value
#     print(flat_dict)
#
# from collections import OrderedDict
# ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
# new_item = ('a', 1)
# new_ordered_dict = OrderedDict([new_item])
# new_ordered_dict.update(ordered_dict)
# print("Updated OrderedDict:", new_ordered_dict)
#
#
# X, Y = map(int, input("Enter two digits (X, Y): ").split(','))
# array = [[0 for j in range(Y)] for i in range(X)]
# for i in range(X):
#     for j in range(Y):
#          array[i][j] = i * j
# for row in array:
#     print(row)
#
#
# input_sequence = input("Enter a comma-separated sequence of words: ")
# words = input_sequence.split(',')
# sorted_words = sorted(words)
# sorted_sequence = ','.join(sorted_words)
# print("Sorted words:", sorted_sequence)
#
# nput_sequence = input("Enter a sequence of whitespace-separated words:")
# words = set(input_sequence.split())
# sorted_words = sorted(words)
# result = ' '.join(sorted_words)
# print("Result:", result)
#
#
#
# sentence = input("Enter a sentence: ")
# letter_count = 0
# digit_count = 0
# for char in sentence:
#    if char.isalpha():
#         letter_count += 1
#    elif char.isdigit():
#         digit_count += 1
# print("LETTERS", letter_count)
# print("DIGITS", digit_count)
#
#
# input_sentence = input("Enter a sentence: ")
# words = input_sentence.split()
# word_freq = {}
# for word in words:
#      word = word.strip('.,?')
#      word = word.lower()
# if word in word_freq:
#    word_freq[word] += 1
# else:
#     word_freq[word] = 1
# sorted_words = sorted(word_freq.items())
#
# for word, frequency in sorted_words:
#     print(f"{word}:{frequency}")
#
# subjects = ["I", "You"]
# verbs = ["Play", "Love"]
# objects = ["Hockey", "Football"]
# sentences = []
# for sub in subjects:
#     for vrb in verbs:
#         for obj in objects:
#             sentence = f"{sub} {vrb} {obj}."
#             sentences.append(sentence)
# for sentence in sentences:
#     print(sentence)
#
#
# def ascci_char(input_str):
#     result = ""
#     for char in input_str:
#         if ord(char)%2==0:
#             result += char.upper()
#         else :
#             result += char.lower()
#
#     return result
# print(ascci_char("ti be not to be"))
# #

# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def getArea(self):
#         return round(math.pi * self.radius**2)
#     def getPerimeter(self):
#         return round(2 * math.pi * self.ra_dius)
#
# circy = Circle(11)
# print(circy.getArea())
# print(circy.getPerimeter())

# #
# def simon_says(list1, list2):
#     return list1[:-1] == list2[1:]
# print(simon_says([1,2,3],[6,7,8]))

# def alphabet_soup(txt):
#     return ''.join(sorted(txt))
# print(alphabet_soup("apple"))


# import math
# def cone_volume(height, radius):
#     if radius == 0:
#         return 0
#         volume = (1/3) * math.pi * (radius**2) * height
#         return round(volume)
#         print(cone_volume(3,3))

#
# def reverse(input_str):
#     reversed_str = input_str[::-1].swapcase()
#     return reversed_str
# print(reverse("hello WORLD"))

# import math
# def area_of_hexagon(x):
#     area = (3 * math.sqrt(3) * x**2) / 2
#     return round(area, 1)
# print(area_of_hexagon(11))

# def is_curzon(num):
#     numerator = 2 ** num + 1
#     denominator = 2 * num + 1
#     return numerator % denominator == 0
# # print(is_curzon(20))

# import math
# def radians_to_degrees(radians):
#     degrees = radians * (180 / math.pi)
#     return round(degrees, 1)
# print(radians_to_degrees(180))