def openreadtxt(file_name):
    data = []
    file = open(file_name, 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        tmp_list = row.split(' ')  # 按‘，'切分每行的数据
        # tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
        data.append(tmp_list)  # 将每行数据插入data中
    return data


if __name__ == "__main__":
    #读取结果文档
    data1 = openreadtxt('dep_list.txt')
    print(data1)
    float_data1=[]
    for i in data1:
        temp_data=[]
        for j  in i :
            temp_data.append(round(float(j),3))
        float_data1.append(temp_data)
    print(float_data1)

    #读取时间文档
    data2 = openreadtxt('ts_list.txt')
    print(data2)
    float_data2=[]
    for i in data2:
        temp_data=[]
        for j  in i :
            temp_data.append(round(float(j),3))
        float_data2.append(temp_data)
    print(float_data2)


    #你要选择那一次BOCA的运行结果  1-10
    sel_it = 1
    #你希望 BOCA 输出小于的 多少值的时间
    want_obj=-1.177
    obj_list=float_data1[sel_it-1]
    time_list=float_data2[sel_it-1]

    jud=0

    for i in range(len(obj_list)):
        if obj_list[i] < want_obj:
            print("在时间",round(time_list[i],2),"出现更好的解")
            jud=1
            break
    if jud==0 :
        print("运行过程中没有比输入值更好的解了")




