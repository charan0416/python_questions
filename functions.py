# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i  # Multiply each number from 1 to n
#     return fact
# print(factorial())
#
# def evenodd(x):
#     if x%2==0:
#         return ("even")
#     else:
#         return ("odd")
#
# x = int(input("enter the number:"))
# print(evenodd(x))

# def missing_num(lst):
#      total_sum = sum(range(1, 11))
#      given_sum = sum(lst)
#      missing = total_sum - given_sum
#      return missing
#
# print(missing_num([1,2,3,4,6,7,8,9,10]))


# def square(x):
#     for x in range (x,x+1):
#         f = x**2
#         return(f)
# print(square(5))


# def div(x,y):
#     z = x/y
#     return z
# print(div(8,2))

# def sort_by_length(lst):
#     return sorted(lst, key=len)
# print(sort_by_length(["apple","banana","cat","doog"]))

# def equal(a, b, c):
#     if a == b == c:
#         return 3
#     elif a == b or b == c or a == c:
#         return 2
#     else:
#         return 0
#
# print(equal(3, 4, 3))

# def dict_to_list(input_dict):
#     sorted_dict = sorted(input_dict.items())
#     result = [(key, value) for key, value in sorted_dict]
#     return result
# print(dict_to_list({
# "D": 1,
# "B": 2,
# "C": 3
# }))


# def mapping(letters):
#     result = {}
#     for letter in letters:
#         result[letter] = letter.upper()
#         return result
# print(mapping(["a", "v", "y", "z"]))

# def vow_replace(string, vowel):
#     vowels = "aeiou"
#     result =""
#     for char in string:
#         if char in vowels:
#             result += vowel
#         else:
#             result += char
#             return result
# print(vow_replace("cheese casserole", "o"))

# def mean(n):
#     n_str = str(n)
#     digit_sum = sum(int(digit) for digit in n_str)
#     digit_count = len(n_str)
#     digit_mean = digit_sum / digit_count
#     return int(digit_mean)
# print(mean(48))


# def society_name(names):
#     secret_name =''.join(sorted([name[0] for name in names]))
#     return secret_name
# print(society_name(["Adam", "Sarah", "Malcolm"]))
#
# def compound_interest(p, t, r, n):
#     a = p * (1 + (r / n)) ** (n * t)
#     return round(a, 2)
#
# print(compound_interest(100, 1, 0.05, 1))

# def alphabet_soup(txt):
#     return ''.join(sorted(txt))
# print(alphabet_soup("hello"))

# def get_budgets(lst):
#     total_budget = sum(person['budget'] for person in lst)
#     return total_budget
# # Test cases
# budgets1 = [
# {'name': 'John', 'age': 21, 'budget': 23000},
# {'name': 'Steve', 'age': 32, 'budget': 40000},
# {'name': 'Martin', 'age': 16, 'budget': 2700}
# ]
# budgets2 = [
# {'name': 'John', 'age': 21, 'budget': 29000},
# {'name': 'Steve', 'age': 32, 'budget': 32000},
# {'name': 'Martin', 'age': 16, 'budget': 1600}
#     ]
# print(get_budgets(budgets1))

# def next_in_line(lst, num):
#     if lst:
#         lst.pop(0)
#         lst.append(num)
#         return lst
#     else:
#         return "No list has been selected"
#
# print(next_in_line([5, 6, 7, 8, 9], 1))

# def triangle(n):
#     if n < 1:
#         return 0
#     else:
#             return n * (n + 1) // 2
# print(triangle(6))
#
# def num_layers(n):
#     initial_thickness_mm = 0.5 # Initial thickness in millimeters
#     final_thickness_mm = initial_thickness_mm * (2 ** n)
#     final_thickness_m = final_thickness_mm / 1000 # Convert millimeter
#     return f"{final_thickness_m:.3f}m"
# print(num_layers(6))
#
# def reverse(value):
#     if isinstance(value, bool):
#         return not value
#     else:
#         return "boolean expected"
# print(reverse(True))





