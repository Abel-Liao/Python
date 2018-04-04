# _*_ coding:utf-8 _*_
height = input("请输入您的身高(M)")
weight = input("请输入您的体重(KG)")
gender = input("请输入您的性别")
age = input("请输入您的年龄")
health = float(weight)/(float(height)**2)
if str(gender) == "男":
    genderMW = 1
else:
    genderMW = 0
fatRate = 1.2 * health + 0.23 * float(age) - 5.4 - 18.8 * genderMW
if health < 18:
    print("您的身体偏瘦")
elif 18 <= health < 25:
    print("您的身体很健康！")
elif 25 <= health < 30:
    print("您超重肥胖")
elif 30 <= health < 35:
    print("您轻度肥胖")
elif 35 <= health < 40:
    print("您中度肥胖")
elif health >= 40:
    print("您重度肥胖")
if genderMW == 1 and 15 < fatRate < 18:
    print("男士，您的体脂率很健康")
elif genderMW == 1 and (fatRate <= 15 or fatRate >= 18):
    print("男士，您的体脂率不健康")
if genderMW == 0 and 25 < fatRate < 28:
    print("女士，您的体脂率很健康")
elif genderMW == 0 and (fatRate <= 25 or fatRate >= 28):
    print(fatRate)
    print("女士，您的体脂率不健康")
