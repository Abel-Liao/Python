# _*_ coding:utf-8 _*_
while True:
    sumNum = 0
    num = input("请输入一个100-999的整数")
    if num.isdigit() and 100 <= int(num) <= 999:
        for i in num:
            # sumNum += int(i) * int(i) * int(i)
             sumNum += int(i) ** 3
        if int(num) == sumNum:
            print('%s是水仙花数' % num)
        else:
            print('%s不是水仙花数' % num)
    else:
        print('请输入数字、整数、100-999的数字')
    out = input("输入exit退出程序")
    if out == "exit":
        break
