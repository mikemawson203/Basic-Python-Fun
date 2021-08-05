# yards = []
# for x in range(3):
#     y = input('enter yards: \n')
#     yards.append(y)
# print(yards)

# yards = []
#
# number of elements



yards  = []
print("Please enter 17 numbers with or without decimals\n")

for num in range(3):
    list_num = float(input("Enter yards thrown:"))
    yards.append(list_num)



touchdowns  = []
print("Please enter 17 numbers with or without decimals\n")

for num in range(3):
    list_num = float(input("Enter td thrown:"))
    touchdowns.append(list_num)
print(sum(yards))
print(sum(touchdowns))

