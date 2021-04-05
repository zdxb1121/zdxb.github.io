from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab, Map, WordCloud, Funnel


def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis([_ for _ in range(2001,2016)])
        .add_yaxis("6.5+级",[41,37,49,41,44,50,59,47,44,60,67,42,56,56,32])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="新世纪以来强震次数统计"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis([str(_) for _ in range(2001,2016)])
        .add_yaxis(
            "6~7级",
            [118,118,123,129,136,147,178,167,129,154,206,126,134,163,84],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .add_yaxis(
            "7+级",
            [16,15,14,15,11,17,20,11,16,23,20,17,19,14,10],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="新世纪以来强震时间分布"))
    )
    return c


def pie_rosetype() -> Pie:
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(["亚欧板块","非洲板块","印度洋板块","太平洋板块","美洲板块"], [66,13,11,56,21])],
            radius=["20%", "60%"],
            center=["30%", "50%"],
            rosetype="area",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(["亚欧板块","非洲板块","印度洋板块","太平洋板块","美洲板块"], [6,0,1,3,1])],
            radius=["20%", "60%"],
            center=["80%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2008年\n五大板块强震次数\n左：6~7级 右：7+级"))
    )
    return c

tab = Tab()
tab.add(bar_datazoom_slider(), "bar-earthquake")
tab.add(line_markpoint(), "line-earthquake")
tab.add(pie_rosetype(), "pie-earthquake")
tab.render("./output/tab_earthquake.html")
