import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 用于读取csv文件，获取好友所在省份信息
def get_city_info(filename):
    lstcity = []
    with open(filename, 'r') as fr:
        reader = csv.reader(fr)
        for i in reader:
            lstcity.append(i[3])
    return lstcity

# 用于绘制柱状图，并展示好友所在省份信息
def plot_city_info(city_info):
    # 用于存储各省份的好友数量
    province_counts = {}
    # 需要统计的省份列表
    provinces = ['山东', '黑龙江', '澳门', '吉林', '江苏', '贵州', '上海', '湖北', '北京', '浙江', '河北', '辽宁']
    for province in provinces:
        province_counts[province] = city_info.count(province)

    # 设置中文字体
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=12)

    # 设置图表样式
    plt.style.use('ggplot')

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(provinces))
    y = [province_counts[p] for p in provinces]
    color = ['lightsteelblue', 'cornflowerblue', 'cadetblue', 'mediumturquoise', 'paleturquoise', 'powderblue', 'skyblue', 'lightskyblue', 'lightblue', 'lavender', 'thistle', 'plum']
    ax.bar(x, y, color=color, alpha=0.8)

    # 添加数据标签
    for i, v in enumerate(y):
        ax.text(i, v + 0.1, str(v), ha='center', fontproperties=font)

    # 设置x轴的刻度标签
    ax.set_xticks(x)
    ax.set_xticklabels(provinces, fontproperties=font)

    # 设置y轴的刻度范围和标签
    ax.set_ylim(0, max(y) * 1.2)
    ax.set_ylabel('好友数量', fontproperties=font)

    # 设置图表标题
    ax.set_title('好友所在省份分布情况', fontproperties=font)

    # 显示网格线
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # 隐藏上、右边框线
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 显示图表
    plt.show()

# 主程序，用于执行上述两个函数
if __name__ == '__main__':
    city_info = get_city_info('friends_information.csv')
    plot_city_info(city_info)
