x=["0 1 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 1 0 1 0 0 1 1 1 1 1 1 1 0 "
   "0 1 0 0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 0 1 0 0 0 0 1 1 0 0 1 1 1 0 0 0 1 1 1 1 0 0 0 1 1 1 1 0 0 1 1 0 1 0 1 1 0",
"1 1 0 0 1 0 0 1 1 1 1 1 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 0 1 1 0"
   " 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 0 1 0 0 0 1 0 0 0 0",
"1 0 1 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 0 1 1 0 1 0 1 1 1 1 0 1 1"
   " 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 1 0 1 0 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0",
"0 0 0 0 1 1 1 1 0 1 1 1 1 0 0 0 1 1 0 0 1 1 1 0 1 1 1 1 1 1 1"
   " 0 0 1 1 0 0 1 1 0 1 1 1 0 0 0 1 1 0 0 1 1 0 0 1 0 1 1 1 0 0 1 0 0 1 0 0 0 0 0 1 1 1 1 0 0 1 0 1 1 1 0 0 1 1 0",
"0 0 0 1 1 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 1 1 1 1 0 1 1 1 0 1 1"
   " 0 0 0 0 1 1 0 1 1 1 1 1 0 0 0 0 1 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 1 1 0 0 1 1 0 1 1 1 1 1 1"

]


resultX=[]
for tempx in x:
    x1_templist=tempx.split(" ")
    x1_list=[]
    for j in range(len(x1_templist)):
        x1_list.append(int(x1_templist[j]))
    resultX.append(x1_list)
print(resultX)
for outx in resultX:
    print("最优序列",outx)