import sqlite3
import pandas as pd
import numpy as np
import csv
import re
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Timeline

#由于播放量和弹幕数中存在“12.3万”这样的字段，因此要处理的话需要做一个转换
def trans(strnum):
    if strnum.endswith("万"):
        return float(strnum[:-1])*10000
    else:
        return float(strnum)

def strf(time):
    lst = re.split("-|/| |]", time)
    if len(lst[1]) != 2:
        lst[1] = "0" + lst[1]
    if len(lst[2]) != 2:
        lst[2] = "0" + lst[2]
    if len(lst[3]) != 8:
        lst[3] = "0" + lst[3]
    return lst[0] + "-" + lst[1] + "-" + lst[2] + " " + lst[3]

def output(connect, title):
    play_list = np.array(pd.read_sql("select * from play", con = connect)).tolist()
    like_list = np.array(pd.read_sql("select * from like", con = connect)).tolist()
    result = {play_list[_][0]:[play_list[_][2:], like_list[_][2:]] for _ in range(len(play_list))}
    
    mindict = {}
    for _ in result:
        if _[:16] in mindict:
            mindict[_[:16]].append(result[_])
        else:
            mindict[_[:16]] = [result[_]]
    for _ in mindict:
        for i in range(70):
            tp = 0
            cp = 0
            tl = 0
            cl = 0
            for j in range(len(mindict[_])):
                if mindict[_][j][0][i] != "NA" and mindict[_][j][0][i] != 0:
                    tp = tp + trans(str(mindict[_][j][0][i]))
                    cp += 1
                if mindict[_][j][1][i] != "NA" and mindict[_][j][1][i] != 0:
                    tl = tl + trans(str(mindict[_][j][1][i]))
                    cl += 1
            mindict[_][0][0][i] = tp/cp if cp != 0 else 0
            mindict[_][0][1][i] = tl/cl if cl != 0 else 0
        mindict[_] = mindict[_][0]
    
    m = Timeline()
    for _ in title:
        bar = (
            Bar()
            .add_xaxis(list(mindict.keys()))
            .add_yaxis("播放量", [mindict[i][0][title.index(_)] for i in mindict])
            .add_yaxis("弹幕数", [mindict[i][1][title.index(_)] for i in mindict])
            .add_yaxis("比值", [(mindict[i][1][title.index(_)]/mindict[i][0][title.index(_)] if mindict[i][0][title.index(_)] != 0 else 0)for i in mindict])
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left='left',pos_top=25), title_opts = opts.TitleOpts(_))
            .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        )
        m.add(bar, _)
    mm = Timeline()
    for _ in title:
        bar = (
            Bar()
            .add_xaxis([mindict[i][0][title.index(_)] for i in mindict])
            .add_yaxis("比值", [(mindict[i][1][title.index(_)]/mindict[i][0][title.index(_)] if mindict[i][0][title.index(_)] != 0 else 0)for i in mindict])
            .set_global_opts(title_opts = opts.TitleOpts(_))
            .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        )
        mm.add(bar, _)
        
    hourdict = {}
    for _ in result:
        if _[:13] in hourdict:
            hourdict[_[:13]].append(result[_])
        else:
            hourdict[_[:13]] = [result[_]]
    for _ in hourdict:
        for i in range(70):
            tp = 0
            cp = 0
            tl = 0
            cl = 0
            for j in range(len(hourdict[_])):
                if hourdict[_][j][0][i] != "NA" and hourdict[_][j][0][i] != 0:
                    tp = tp + trans(str(hourdict[_][j][0][i]))
                    cp += 1
                if hourdict[_][j][1][i] != "NA" and hourdict[_][j][1][i] != 0:
                    tl = tl + trans(str(hourdict[_][j][1][i]))
                    cl += 1
            hourdict[_][0][0][i] = tp/cp if cp != 0 else 0
            hourdict[_][0][1][i] = tl/cl if cl != 0 else 0
        hourdict[_] = hourdict[_][0]
    
    h = Timeline()
    for _ in title:
        bar = (
            Bar()
            .add_xaxis(list(hourdict.keys()))
            .add_yaxis("播放量", [hourdict[i][0][title.index(_)] for i in hourdict])
            .add_yaxis("弹幕数", [hourdict[i][1][title.index(_)] for i in hourdict])
            .add_yaxis("比值", [(hourdict[i][1][title.index(_)]/hourdict[i][0][title.index(_)] if hourdict[i][0][title.index(_)] != 0 else 0)for i in hourdict])
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left='left',pos_top=25), title_opts = opts.TitleOpts(_))
            .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        )
        h.add(bar, _)
    hh = Timeline()
    for _ in title:
        bar = (
            Bar()
            .add_xaxis([hourdict[i][0][title.index(_)] for i in hourdict])
            .add_yaxis("比值", [(hourdict[i][1][title.index(_)]/hourdict[i][0][title.index(_)] if hourdict[i][0][title.index(_)] != 0 else 0)for i in hourdict])
            .set_global_opts(title_opts = opts.TitleOpts(_))
            .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        )
        hh.add(bar, _)
    p = Page()
    p.add(m,h)
    p.render("../web/数据随时间变化.html")
    pp = Page()
    pp.add(mm,hh)
    pp.render("../web/比值随播放量变化.html")
    
with open("../other/弹幕数.csv", "r") as file:
    reader = csv.reader(file)
    title = [row for row in reader][0][1:]

conn = sqlite3.connect("../other/bilibili.db")
output(conn, title)