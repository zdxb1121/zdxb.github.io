from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


c = (
    Geo()
    .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
        "",
        [("绥芬河", 16), ("北京", 2),  ("上海", 1), 
         ("大连", 3), ("南京", 1), ("杭州", 1), ("哈尔滨", 1), ("四川", 1), 
         ("西藏", 1), ("阜新", 3), ("天津", 2), ("辽阳", 20)
        ],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        itemstyle_opts=opts.ItemStyleOpts(color='white'),
    )
    .add(
        "我的",
        [("绥芬河", "哈尔滨"), ("哈尔滨", "绥芬河"), ("绥芬河", "北京"), ("北京", "上海"), ("上海", "杭州"), ("杭州", "绥芬河"),
         ("绥芬河", "大连"), ("大连", "太原"), ("太原", "大连"), ("大连", "天津"),
         ("天津", "大连"), ("大连", "南京"), ("南京", "上海"), ("上海", "大连"),
         ("大连", "阜新"),  ("阜新", "大连"), ("大连", "北京")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=5, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
        color = 'red',
    )
    .add(
        "我妈的",
        [("阜新", "辽阳"), ("辽阳", "绥芬河"), ("绥芬河", "哈尔滨"), ("哈尔滨", "绥芬河"), ("绥芬河", "北京"), ("北京", "上海"), ("上海", "杭州"), ("杭州", "绥芬河"),
         ("绥芬河", "大连"),  ("大连", "南京"), ("南京", "上海"), ("上海", "大连"),
         ("大连", "阜新"),  ("阜新", "大连"), ("大连", "四川"), ("四川", "西藏"), ("西藏", "大连")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=5, color="black"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
        color = "blue"
     )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="我和我妈的旅行图"))
    
    .render('./output/geo_travel_with_mom.html')
)


