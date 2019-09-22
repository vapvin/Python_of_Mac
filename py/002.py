# -*-Encoding: UTF-8 -*-

# my_bool = True
# my_bool2 = False
# my_bool3 = 1 < 2
# my_bool4 = 1 == 2

# print(my_bool)
# print(my_bool2)
# print(my_bool3)
# print(my_bool4)

# my_con1 = 1 < 2 and 2 < 3
# my_con2 = 1 < 2 and 2 > 3
# my_con3 = 3 < 4 or 4 > 5
# my_con4 = not True

# print(my_con1)
# print(my_con2)
# print(my_con3)
# print(my_con4)

# yours = "Kyu"
# if yours == "Hyun":
#     print("당신이 Hyun이군요")
#     print("Nice to meet you")
# elif yours == "Kyu":
#     print("당신이 Kyu이군요")
#     print("Nice to meet you")
# else:
#     print("당신이 HynKyue이군요")
#     print("Nice to meet you")

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# count = 0
# while count < 5:
#     count += 1
#     if count % 2 == 1:
#         continue
#     print(count)

while True:
    name = input('당신의 이름은?')
    if name == '종료':
        print('종료합니다.')
        break
    print('{}님, 안녕!'.format(name))
