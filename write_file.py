# task1
#with open(r'C:\Users\HUAWEI\Desktop\poem.txt','w', encoding='utf-8') as f:
#    f.write('我欲乘风归去，\n')
#    f.write('又恐琼楼玉宇，\n')
#    f.write('高处不胜寒。\n')




# task2
#with open(r'C:\Users\HUAWEI\Desktop\poem.txt','a', encoding='utf-8') as f:
#    f.write('起舞弄清影，\n')
#    f.write('何似在人间。')




#practise
with open(r'C:\Users\HUAWEI\Desktop\poem2.txt','w', encoding='utf-8') as f:
    f.write('戍鼓斷人行，邊秋一雁聲。\n')
    f.write('露從今夜白，月是故鄉明。\n')
    f.write('有弟皆分散，無家問死生。\n')
    f.write('寄書長不達，況乃未休兵。\n')

with open(r'C:\Users\HUAWEI\Desktop\poem2.txt','a', encoding='utf-8') as f:
    f.write('——月夜憶舍弟[唐]杜甫\n')

with open(r'C:\Users\HUAWEI\Desktop\poem2.txt','r', encoding='utf-8') as f:
    lines = f.readlines()
    for i , line in enumerate(lines,start = 1):
        print(f'第{i}行:{line.strip()}')

