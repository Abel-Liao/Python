# _*_ coding:utf-8 _*_
while True:
    num1 = input("请输入第一个数字")
    # if not(num1.isdigit()):
    #     print("请输入数字")
    #     continue
    try:
        float(num1)
    except ValueError:
        continue
    num2 = input("请输入第二个数字")
    # if not(num2.isdigit()):
    #     print("请输入数字")
    #     continue
    try:
        float(num2)
    except ValueError:
        continue
    else:
        print(eval(num1) + eval(num2))

