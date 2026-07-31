#1、第一种写法
#f = open(r'C:\Users\HUAWEI\Desktop\data.txt' , 'r', encoding='utf-8')
#content = f.read()
#print(content)
#f.close()


#2、第二种写法
#with open(r'C:\Users\HUAWEI\Desktop\data.txt' , 'r', encoding='utf-8') as f:
#    print(f.readline())
#    print(f.readline())



#3、第三种写法
with open(r'C:\Users\HUAWEI\Desktop\data.txt' , 'r', encoding='utf-8') as f:
#   print(f.readlines())
    lines = f.readlines()
    for line in lines:
        print(line)

