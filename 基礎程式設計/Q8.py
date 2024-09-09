paint = (float(input("輸入公升:")))
print(paint)
paint = paint* 0.26418
print("%.1f"%paint , "加侖")
# %.1 2 3 %後面數字為取小數點第幾位
print("{:.1f}".format(paint))
#大括弧 裡面冒號 :.數字  寫入格式 .format 就會轉換成想要的格式
#({:.2f}.format(變數))
print("{:.4f}".format(paint))
