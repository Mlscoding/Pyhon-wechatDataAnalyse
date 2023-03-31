import csv
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# 1.读取csv文件，把性别信息读取出来
def getSex(filename):
    lstsex = []
    with open(filename, 'r') as fr:
        reader = csv.reader(fr)
        for i in reader:
            lstsex.append(i[4])
    return lstsex


# 2.性别pyechart可视化
def VisualSexpyechart(lstsex):
    sex = dict()
    # 2.1提取好友性别信息，从1开始，因为第0个是自己
    for f in lstsex[1:]:
        if f == '1':  # 男
            sex["man"] = sex.get("man", 0) + 1
        elif f == '2':  # 女
            sex["women"] = sex.get("women", 0) + 1
        else:  # 未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 在屏幕上打印出来
    total = len(lstsex[1:])
    # 2.2打印出自己的好友性别比例
    plt.figure(figsize=(6, 9))
    labels = [u'男性好友', u'女性好友', u'性别不明']
    sizes = [sex['man'], sex['women'], sex['unknown']]
    colors = ['cornflowerblue', 'lightcoral', 'silver']
    explode = (0.05, 0, 0)
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1,
                                      autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size(30)
    for t in p_text:
        t.set_size(20)
    plt.axis('equal')
    plt.legend()
    plt.show()


# 3.执行主程序，得到所有好友性别
VisualSexpyechart(getSex("friends_information.csv"))
