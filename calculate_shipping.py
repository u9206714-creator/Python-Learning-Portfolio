#3、计算快递费用
def calculate_shipping(weight):
    if weight <= 1:
        shipping_cost = 8
    elif weight <= 5:
        shipping_cost = 15
    elif weight <= 10:
        shipping_cost = 25
    else:
        shipping_cost = 40
    print(f'快递重量为{weight}kg')
    return shipping_cost
money = calculate_shipping(34)
print(f'本次运费为{money}元')

