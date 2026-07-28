#python函数学习（上） ->不做代码复读机
#求扇形面积计算公式
'''
def calculate_sector(central_angle,radius):
    sector_area = central_angle / 360*3.14*radius**2
    print(f'此扇形的面积为：{sector_area}')

calculate_sector(160,30)
'''


#python函数（下）->学习return的作用
#1、写一个计算BMI的函数
'''
def calculate_BMI(weight,height):
    BMI = weight/(height**2)
    if BMI <= 18.5:
        BMI_type = '偏瘦' 
    elif 18.5 < BMI <= 25:
        BMI_type = '正常'
    elif 25 < BMI <= 30:
        BMI_type = '偏胖'    
    else:
        BMI_type = '肥胖'
    print(f'你的BMI分类为{BMI_type}')
    return BMI
result = calculate_BMI(20,14)
print(result)
'''





