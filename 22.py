# import random
#
# total = 0
#
# number = random.randint(1, 100)
#
# while True:
#
#     user_input = input("请输入数字：")
#
#     total += 1
#
#     if int(user_input) == number:
#         print("猜对了")
#         print(f"你猜了 {total} 次")
#         break
#
#     elif int(user_input) < number:
#         print("小了")
#
#     elif int(user_input) > number:
#         print("大了")

# s1 ="hello"
# s2 = "world"
# s3 ="""
# hello : world
# slinjsjdlfijwif~
# """
# print(s1);
# print(s2);
# print(s3);
#
#
# msg ='I love you\'s good';
# print(msg);


#
# s1 ="hello"
# s2 = "world"
#
# print("丹佛i五年打开的咯额是%s , 去微软推哦怕 %s"%(s1,s2))
# print("丹佛i五年打开的咯额是{} , 去微软推哦怕 {}".format(s1,s2))
# print("去微软{} , 推哦怕的{}, 风格和健康".format(s1,s2))
# print(f"去微软推哦{s1}怕时代法国红酒看{s2}来自行车v吧")

# name=input("请输入你的名字：")
# print(f"你好，{name}")
# i= 100;
# if i>=100:
#     print("大于huodeyu100")
# elif i<50:
#     print("小于50")
#
# print("请输入账号")
# username = input()
# print("请输入密码")
# password = input()
# if username == "admin" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败 密码错误")


# year =int(input("请输入年份："))
# if (year%100 !=0 and year%4==0) or year%400==0:
#      print(f"{year}是闰年")
# else:
#      print(f"{year}不是闰年");
#
# numbre=int(input("请输入一个数字："))
# if numbre >0:
#     print("正数")
# elif numbre<0:
#     print("负数")
# else:
#     print("零")

# nu1=int(input("请输入第一个边："))
# nu2=int(input("请输入第二个边："))
# nu3=int(input("请输入第三个边："))
# if nu1==nu2==nu3:
#     print("等边三角形")
# elif nu1==nu2 or nu1==nu3 or nu2==nu3:
#     print("等腰三角形")
# else:
#     print("普通三角形")

#
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# oper = input("请输入运算符：")
# match oper:
#     case "+":
#         print({num2}+{num1}+{num1+num2})
#     case "-":
#         print({num2}+{num1}+{num1-num2})
#     case _:
#         print("输入错误")

# total =0
# i=1
# while i<=100:
#     if i%2==0:
#         total+=i
#
#         i+=1
#
# print(total)

# m =int(input("请输入长方形的长度："))
#
# n =int(input("请输入长方形的宽度："))
# for i in range(n):
#     for j in range(m):
#       print("*",end="  ")
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#     print()

# s =[84,30,102,2029,2039,"hello","world",True]
# print(s[0:4:1])
# print(s[0:4:3])

# for item in s:
#     print(item)
# print(s[0])
# print(s[1])
# print(s[-2])
#
# s[4]="ajdjfshdfdsf"
# print(s[4])
# print(type(s))
# print(s[0:3])
# s[5]="slkjfdlsk"
# print(s)
#
# del  s[3]
# print(s)
# numa =[]
# for i in range(10):
#     num=int(input("请输入数字："))
#     numa.append(num)
# print("排序后的数字列表",numa)
# print("最小值",numa[0])
# print("最大值",numa[-1])
# print("平均值",sum(numa)/len(numa))
numa1=[10,11,12,13,14,15,16,17,18,]
numa2=[20,21,22,23,24,25,26,28,28,]

# a22= numa2+numa1;
# print(a22)
# for num in numa2:
#     numa1.append(num)
# print(f"合并后的原始列表{numa1}")
#
# numlist=[]
# for num in numa1:
#     numlist.append(num)
#     print(f"合并后的新列表{numlist}")

# num_list =[]
# for i in range(1,21):
#     num_list.append(i**2)
# print (num_list)
# name ="python"
# print(name)
# print(len(name))
# s ="python"
# print(s[0])
# print(s[3])
# print(s[5])

# s = "Python"
#
# print(s[0:3])
#
# print(s[2:6])
#
# print(s[:2])
#
# print(s[3:])
# l = "hello"
# print(len(l))
# print(l[:1])
# print(l[6])
# name = "Python"
# print(name)
# print(len(name))
# print(name[0])
# print(name[5])
# city = "Beijing"
# print(city)
# print(len(city))
# print(city[0])
# print(city[6])
# print(city[0:3])
# print(city[4:6])
# language = "Python"
# print(len(language))
# print(language[0])
# print(language[5])
# print(language[0:2])
# print(language[3:5])
#
# name = input("请输入你的名字：")
# print("你好，" + name)
# print("你名字长度是"+len(name))
# print("你名字的第一个字符是"+name[1])
# print("你名字的最后一个字符是"+name[-1]   )
#
# i="ChatGPT"
# print(i[0])
# print(i[1])
# print(i[0:2])
# print(i[3:5])

# fruit = "watermelon"
# print("水果:"+fruit)
# print("长度",len(fruit))
# print("第一个字符："+fruit[1])
# print("最后一个字符："+fruit[-1])
# #
# name = input("请输入你的名字：")
# print("你好，" + name)
# print("你名字长度是"+len(name))
# print("你的第一个字:"+name[1])
# print("你的第一个字:"+name[-1])
#
# city = input("请输入城市：")
# print(city[0:3])
# print(city[-1:-4])


# word = input("请输入一个英文单词：")
# print(len(word))
# print(word[0])
# print(word[-1])
# print(word[0:4])
# print(word[-1:-4])
#
#
# a="chatgpt"
# print(a[0])
# print(a[1])
# 一直到6可以吗

# book = "Harry Potter"
# print(len(book))
# print(book[1])
# print(book[-1])
# print("正数第六",book[0:6])
# print("最后五个",book[-6:-1])

# username = input("请输入用户名：")
# print("欢迎",username)
# print(len(username))
# print("第一个字符",username[0])
# print("最后字符",username[-1])
# print("正数三个",username[0:3])
# print("倒数三个",username[-4:-1])
# 你好，Alice！
#
# 你的名字长度：5
#
# 第一个字符：A
#
# 最后一个字符：e
# name = input("请输入你的名字：")
# print("hello ",name)
# print("you is name 长",len(name) )
# print("第一个字符",name[0])
# print("最后一个字符",name[-1])

# name =input("请输入你的名字：")
# age =int(input("请输入你的年龄："))
#
#
# if age >= 18 | len(name)>=3 :
#     print("可以进入")
#     print("你的名字长度",len(name))
#     print("你的名字的第一个字符",name[0])
#     print("你的名字的最后一个字符",name[-1])
# else:
#     print("不可以进入")

# 年龄>=18
#
# 并且
#
# 名字长度>=3

# name =input("请输入你的名字：")
# age =int(input("请输入你的年龄："))
#
#
# if age >= 18 and len(name)>=3  and len(name)<=20:
#     print("用户名字",name)
#
#     print("注册成功")
# else:
#     print("注册失败")
#     print("用户名字限制为20字符以内 年龄要大于18岁")


# 年龄>=18
#
# 并且
#
# 名字长度>=3

# age =int(input("请输入你的年龄："))
# name =input("请输入你的名字：")
# if age>=18 and 3<=len(name)<=20:
#     # 上面那个条件是抄的你的
#     print("用户名字",name)
#     print("注册成功")
# elif age<18:
#     print("年龄太小不满18")
# elif len(name)<3:
#     print("名字太短")
# else:
#     print("名字太长")
# age =int(input("请输入你的年龄："))
# name =input("请输入你的名字：")
# if age>=18 and 3<=len(name)<=20:
#     print("用户名字",name)
#     print("注册成功")
# elif age<18:
#     print("年龄太小不满18")
# elif len(name)<3:
#     print("名字太短")
# else:
#     print("名字太长")
# name =input("请输入你的名字：")
# age =int(input("请输入你的年龄："))
# if name=="admin" and age>=18:
#     print("管理员")
# else:
#     print("登陆失败")
# name =input("请输入你的名字：")
# password =input("密码：")
# if name=="admin" and password=="123456":
#     print("登陆成功")
# else:
#     print("登陆失败")

# name = input("请输入你的名字：")
# print("你的名字是"+name)
# print("你的名字长度"+len(name))

# name = input("请输入你的名字：")
# age = int(input("请输入你的年龄："))
#
# if age>=18 :
#     print("恭喜进入")
# else :
#     print("未成年禁止进入")
# name =input("请输入你的名字：")
# a=(len(name))
# print("你的名字长度",a)

# print("10"*10)
# name =input("你的名字是什么")
# age =int(input ("请输入你的年龄"));
# if age>=18  and len(name)>=3:
#     print("可以进入")
# else:
#     print("年龄不够或 名字太短")

# colors = ["red", "blue", "green"]
# colors[0]="a"
# print(colors)
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)
# names = ["tom","jack","alice"]
# names.append("a")
# print(names)
#
# names = ["Tom", "Jack", "Alice"]
# for name in names:
#     print(name)

# shopping = []
# for i in  range(3):
#     item =input("请输入"+str(i+1)+"商品名称：")
#     shopping.append(item)
# print(shopping)

# chenji =[]
# for i in range(3):
#      a=int(input("请输入"+str(i+1)+"成绩："))
#
#      chenji.append(a)
#      if a>=60:
#          print("及格")
#      else:
#          print("不及格")
# print(i,"是及格的")
# a1 =int(input("请输入数字："))
# print("这个数字的平方是",a1*a1)
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)
# name = input("请输入你的名字：")
# age =int(input("请输入你的年龄："))
# print("你的名字是"+name)
# print("你的年龄是"+str(age))
# num= int(input("请输入一个数字："))
# if num/2==0:
#     print("偶数")
# else:
#         print("奇数")
# def add(a, b):
#     result = a + b
#     return result
# def double_number(num):
#     return num * 2
# print(double_number(5))
# def check_username(name):
#      if len(name)>=3 and len(name)<=10:
#          print("文本")
#          return True
#      else:
#          print("文本")
#          return False;
#
#
# print(check_username("李"))
# print(check_username("王小二"))
# print(check_username("这是一个超长的名字"))
nums = [10, 20, 30]

# def show(numbers):
#     print(numbers)
#
# show(nums)
numbers = [10, 20, 30]
def sum_numbers(numbers):
 total = 0
 for number in numbers:
    total = total + number
 return total
a1 = sum_numbers(numbers)
print(a1)


























































































































































































































































































































































































































































































































































































































































































































































