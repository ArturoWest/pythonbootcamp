import datetime

now = datetime.datetime.today()

print(now)

print(now.day)

print(now.weekday())

x = datetime.datetime.strptime("2018/11/18", "%Y/%m/%d")

print(x)

my_birthday = datetime.datetime(1980, 2, 11)
print(my_birthday.weekday())


delta = now - my_birthday

for i in range(20):
    print(now + datetime.datetimedelta(hours=i))