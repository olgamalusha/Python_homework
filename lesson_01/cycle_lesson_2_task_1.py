# employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
# result = f"{employee_list[1]}, {employee_list[-2]}"
# print(result)
# print(employee_list[1] + ", " + employee_list[-2])



#  def dev_by_three(number):
#     if number % 3 == 0:
#         return 'Да'
#     else:
#         return 'Нет'
    
# my_number = 7
# result = dev_by_three(my_number)
# print(f"Делится ли на три {my_number}? - {result}")




# def dev_by_three(number):
#      return 'Да' if number % 3 == 0 else 'Нет'

# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делится ли на три {num}? - {result}")



# import math
# def min_boxes(items_count):
#     return math.ceil(items_count / 5)
# user_items = int(input("Введите количество предметов: "))
# result = min_boxes(user_items)
# print(f"Для {user_items} предметов потребуется коробок: {result}")


# import math
# def min_boxes(items_count):
#     return math.ceil(items_count / 5)
# items = 12
# result = min_boxes(items)
# print(f"Для {items} предметов потребуется коробок: {result}")

# items = 25
# result = min_boxes(items)
# print(f"Для {items} предметов потребуется коробок: {result}")


# import math
# def min_boxes(items_count):
#     return math.ceil(items_count / 5)

# test_cases = [0, 1, 5, 6, 10, 11, 99]
# for items in test_cases:
#     result = min_boxes(items)
#     print(f"предметов: {items} -> Потребуется коробок: {result}")



# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - делится на 2, но не на 4")
#         else:
#             print(i)

# check_divisibility(26)



# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return "I квартал"
#     elif 4 <= month <= 6:
#         return "II квартал"
#     elif 7 <= month <= 9:
#         return "III квартал"
#     elif 10 <= month <= 12:
#         return "IV квартал"
    
# print(quarter_of_year(10))



# def quarter_of_year(month):
#     return (month - 1) // 3 + 1
# print(quarter_of_year(8))



# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return "I квартал"
#     if 4 <= month <= 6:
#         return "II квартал"
#     if 7 <= month <= 9:
#         return "III квартал"
#     if 10 <= month <= 12:
#         return "IV квартал"
#     return "Неверный номер месяца"

# month = int(input("Введите номер месяца (1-12): "))
# print(quarter_of_year(month))



# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# for number in lst:
#     if number > 15 and number % 3 == 0:
#         print(number)


lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

result = [x for x in lst if x > 15 and x % 3 == 0]

print(result)