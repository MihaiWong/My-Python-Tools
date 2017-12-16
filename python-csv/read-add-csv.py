import csv

'''
应用于修改csv 在每行末尾插入数据  
参数：filepath : C:/Users/lenovo/Desktop/
      file = 1.csv
返回 modify success
'''


def add_csv(file_path, filex):
    fileName = file_path + filex
    # 读取文件
    with open(fileName) as f:
        # 获取csv内容
        reader = csv.reader(f)
        headers = next(reader)
        print("使用下标进行访问")
        # 打开新的存储新生成的csv文件
        # 注意： newline='' 抑制文本模式换行处理。在Windows上，如果没有这样做，将会写入\r\r\n文件行尾，而不是正确的\r\n
        c = open(file_path + 'train.csv', 'w', newline='')
        # 转换为writer类型
        writer = csv.writer(c)
        i = 0
        # length = len(list(reader))
        # 遍历 获取每行csv的数据list
        for row in reader:
            print(row)
            # 添加一个数据
            row.append(str(i // 20))
            # print(i)
            # print(row)
            print('------------------')
            if (i // 20) < 4:
                # 写入写的csv文件
                writer.writerow(row)
            i = i + 1
    return 'modify success'


if __name__ == '__main__':
    file_path = 'C:/Users/lenovo/Desktop/'
    files = '1.csv'
    add_csv(file_path, files)
