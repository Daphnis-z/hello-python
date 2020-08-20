import calendar

print("Hello World !!")
print("你好，世界 ！！")
str = "Daphnis"
print(str[-7])
nums = [5, 9, 11, 2, 3]
num = 5
if (num in nums):
    print("D在序列里")


def printCalendar(year, month):
    cal = calendar.month(year, month)
    print("以下输出%d年%d月份的日历:" % (year, month))
    print(cal)


printCalendar(2018, 10)
