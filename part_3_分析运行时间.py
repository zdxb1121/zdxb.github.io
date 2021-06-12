import pandas as pd
import numpy as np
import re
import csv
from pyecharts import options as opts
from pyecharts.charts import Bar, Page
#定义一个
def strf(time):
    lst = re.split("-|/| |]", time)
    if len(lst[1]) != 2:
        lst[1] = "0" + lst[1]
    if len(lst[2]) != 2:
        lst[2] = "0" + lst[2]
    if len(lst[3]) != 8:
        lst[3] = "0" + lst[3]
    return lst[0] + "-" + lst[1] + "-" + lst[2] + " " + lst[3]

def output(timedict, filename):
    #得到整体的运行时间平均值和方差
    time_mean = np.mean([timedict[_] for _ in timedict])
    time_std = np.std([timedict[_] for _ in timedict], ddof = 1)
    print(time_mean, time_std)
    #将每分钟的数据整合到一起并求均值和方差
    mindict = {}
    for _ in timedict:
        if (_[:16] in mindict.keys()) is False:
            mindict[_[:16]] = [timedict[_]]
        else:
            mindict[_[:16]].append(timedict[_])
    for _ in mindict:
        if len(mindict[_]) >= 4:
            std = np.std(mindict[_], ddof = 1)
        else:
            std = 0
        mindict[_] = [np.mean(mindict[_]), std]
    #将每小时的数据整合到一起并求均值和方差
    hourdict = {}
    for _ in timedict:
        if (_[:13] in hourdict.keys()) is False:
            hourdict[_[:13]] = [timedict[_]]
        else:
            hourdict[_[:13]].append(timedict[_])
    for _ in hourdict:
        if len(hourdict[_]) >= 4:
            std = np.std(hourdict[_], ddof = 1)
        else:
            std = 0
        hourdict[_] = [np.mean(hourdict[_]), std]
    
    minbar = (
        Bar()
        .add_xaxis(list(mindict.keys()))
        .add_yaxis("均值", [mindict[_][0] for _ in mindict])
        .add_yaxis("方差", [mindict[_][1] for _ in mindict])
        .set_global_opts(title_opts = opts.TitleOpts("每分钟"))
        .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
    )
    
    hourbar = (
        Bar()
        .add_xaxis(list(hourdict.keys()))
        .add_yaxis("均值", [hourdict[_][0] for _ in hourdict])
        .add_yaxis("方差", [hourdict[_][1] for _ in hourdict])
        .set_global_opts(title_opts = opts.TitleOpts("每小时"))
        .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
    )
    
    page = Page()
    page.add(minbar, hourbar)
    page.render("../web/" + filename + ".html")
    
#将得到的运行时间的csv文件全部整合到一个dataframe中
df = pd.read_csv("../other/爬取运行时间.csv")
timedict = {strf(_[0]):_[1] for _ in df.values}
print(len(timedict))

output(timedict, "全部运行时间")

with open("../other/弹幕数.csv", "r") as file:
    reader = csv.reader(file)
    timelist = list(timedict).copy()
    crow = 0
    for row in reader:
        if len(set(row)) == 2:
            del timedict[timelist[crow - 1]]
        crow += 1
output(timedict, "筛选后的运行时间")