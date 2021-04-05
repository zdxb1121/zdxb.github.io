from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
   

c = (
    Map()
    .add("2008年发生的5.5级以上地震的次数", 
         [('United States',20),('China',33),('Japan',23),("Russia",19),("Chile",26),("Indonesia",73),("Solomon Is.",37),('Philippines',24),("Australia",1),("Papua New Guinea",16),("Iceland",1)], 
         maptype="world",
         is_map_symbol_show=True, # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=75),
    )
)

c.render('./output/map_earthquake.html')
