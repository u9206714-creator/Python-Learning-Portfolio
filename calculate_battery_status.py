#4、计算手机电量状态
def battery_status(power):
    if power >= 80:
        status = 'enough'
    elif power >= 50:
        status = 'normal'
    elif power >= 20:
        status = 'a bit low'
    else:
        status = 'please charge your phone now'
    print(f'your battery power is {power}%')
    return status
electricity = battery_status(71) 
print(f'your battery status is {electricity}')

