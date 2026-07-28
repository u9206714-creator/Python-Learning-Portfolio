#5、购物结算
def discount(price, vip):
    if vip == False:
        final_price = price 
    elif vip == True and price >= 200:
        final_price = price*0.8
    elif vip == True and 0 < price <= 200:
        final_price = price*0.9
    else:
        final_price = 'this is a wrong number' 
    return final_price
result = discount(483,True)
print(f'优惠后的价格为{result}')



