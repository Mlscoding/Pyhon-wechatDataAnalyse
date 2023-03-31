import csv
from pyecharts import options as opts
from pyecharts.charts import Pie


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
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(['男性好友', '女性好友', '性别不明'], [sex['man'], sex['women'], sex['unknown']])],
            radius=["30%", "70%"],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="微信好友性别比例",
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(font_size=20),
            ),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_left="80%", orient="vertical", item_height=15
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("friends_sex.html")
    )


# 3.执行主程序，得到所有好友性别
VisualSexpyechart(getSex("friends_information.csv"))
