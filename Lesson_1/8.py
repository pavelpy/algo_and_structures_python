# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.


year = int(input("введите год: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("введённый вами год високосный")
else:
    print("введённый вами год не високосный")
