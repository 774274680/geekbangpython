# 从1 到 10  所有偶数的平方
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append( i*i )


print(alist)

#列表推导式
# 列表1-10，偶数的话就求平方
blist = [i*i for i in range(1, 11) if(i % 2) == 0]

print(blist)

z_num = {}
for i in zodiac_name:
    z_num[i] = 0

z_num = {i:0 for i in zodiac_name}

#
obj = {"name":"haha","age":10}
for i in obj:
    print(i)

#字典推导式
olist = {i for i in obj}
