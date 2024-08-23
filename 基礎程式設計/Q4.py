#總分 平均乘積 
ch , en , ma = map(int,input("ch= en = ma =").split())# int 表示 整點數 split作切割 
tot = ch + en + ma 
avg = tot / 3.0
print(tot)
print("%.0f"%avg)


