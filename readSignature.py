import csv

with open('friends_information.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # 遍历每一行数据
    for row in reader:
        # 获取签名数据
        signature = row[5]
        # 如果签名不为空，则保存到txt文件中
        if signature:
            with open('chinese.txt', 'a') as f:
                f.write(signature + '\n')
