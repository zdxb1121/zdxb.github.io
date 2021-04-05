from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()

geo.add_coordinate(name="12-09T06:24:01",longitude=-176.85, latitude=-31.27)
geo.add_coordinate(name="11-24T09:03:00",longitude=154.29, latitude=54.22)
geo.add_coordinate(name="11-20T23:29:07",longitude=117.47, latitude=-6.68)
geo.add_coordinate(name="11-16T17:02:32",longitude=122.16, latitude=1.35)
geo.add_coordinate(name="10-19T05:10:34",longitude=-173.79, latitude= -21.88)
geo.add_coordinate(name="10-16T19:41:33",longitude=-92.33, latitude=14.54)
geo.add_coordinate(name="10-05T15:52:50",longitude=73.79, latitude=39.55)
geo.add_coordinate(name="09-29T15:19:30",longitude=-177.63, latitude=-30.09)
geo.add_coordinate(name="09-11T00:20:52",longitude=143.82, latitude=41.94)
geo.add_coordinate(name="09-11T00:00:02",longitude=127.44, latitude=1.88)
geo.add_coordinate(name="09-10T13:08:14",longitude=-38.68, latitude=8.12)
geo.add_coordinate(name="09-08T18:52:09",longitude=166.98, latitude=-13.51)
geo.add_coordinate(name="08-25T13:22:01",longitude=83.65, latitude=31.06)
geo.add_coordinate(name="07-23T15:26:20",longitude=141.50, latitude=39.79)
geo.add_coordinate(name="07-19T09:27:04",longitude=164.52, latitude=-11.07)
geo.add_coordinate(name="07-19T02:39:29",longitude=142.25, latitude=37.54)
geo.add_coordinate(name="07-05T02:12:06",longitude=152.86, latitude=53.94)
geo.add_coordinate(name="06-30T06:17:43",longitude=-21.97, latitude=-58.28)
geo.add_coordinate(name="06-27T11:40:15",longitude=91.84, latitude=10.99)
geo.add_coordinate(name="06-13T23:43:46",longitude=140.73, latitude=39.15)
geo.add_coordinate(name="06-01T14:31:01",longitude=150.04, latitude=-59.59)
geo.add_coordinate(name="05-23T19:35:35",longitude=-34.89, latitude=7.359)
geo.add_coordinate(name="05-12T06:27:59",longitude=103.37, latitude=31.06)
geo.add_coordinate(name="05-09T21:51:31",longitude=143.26, latitude=12.53)
geo.add_coordinate(name="05-07T16:45:21",longitude=141.50, latitude=36.23)
geo.add_coordinate(name="05-02T01:33:35",longitude=-177.49, latitude=51.85)
geo.add_coordinate(name="04-24T12:14:50",longitude=-23.52, latitude=-1.153)
geo.add_coordinate(name="04-16T05:54:21",longitude=-179.10, latitude=51.87)
geo.add_coordinate(name="04-15T22:59:54",longitude=-179.36, latitude=51.90)
geo.add_coordinate(name="04-12T00:30:12",longitude=158.54, latitude=-55.59)
geo.add_coordinate(name="04-09T12:46:12",longitude=168.90, latitude=-20.03)
geo.add_coordinate(name="03-20T22:32:58",longitude=81.50, latitude=35.54)
geo.add_coordinate(name="03-03T14:11:15",longitude=125.71, latitude=13.42)
geo.add_coordinate(name="03-03T09:31:06",longitude=153.12, latitude=46.38)
geo.add_coordinate(name="02-25T21:02:19",longitude=99.80, latitude=-2.24)
geo.add_coordinate(name="02-25T18:06:05",longitude=99.86, latitude=-2.38)
geo.add_coordinate(name="02-25T08:36:33",longitude=99.92, latitude=-2.48)
geo.add_coordinate(name="02-24T14:46:23",longitude=99.92, latitude=-2.42)
geo.add_coordinate(name="02-23T15:57:19",longitude=-23.50, latitude=-57.22)
geo.add_coordinate(name="02-20T08:08:31",longitude=95.96, latitude=2.76)
geo.add_coordinate(name="02-14T12:08:57",longitude=21.83, latitude=36.38)
geo.add_coordinate(name="02-14T10:09:23",longitude=21.67, latitude=36.51)
geo.add_coordinate(name="02-12T12:50:19",longitude=-94.24, latitude=16.43)
geo.add_coordinate(name="02-10T12:22:03",longitude=-25.59, latitude=-60.78)
geo.add_coordinate(name="02-08T09:38:13",longitude=-41.90, latitude=10.72)
geo.add_coordinate(name="01-15T17:52:16",longitude=-179.58, latitude=-21.98)
geo.add_coordinate(name="01-05T11:01:05",longitude=-130.75, latitude=51.25)

# 添加数据项（设置地图范围）
geo.add_schema(maptype="world")

geo.add("",
        [   ("12-09T06:24:01", 6.7),
            ("11-24T09:03:00", 7.3),
            ("11-20T23:29:07", 6.5),
            ("11-16T17:02:32", 7.3),
            ("10-19T05:10:34", 6.9),
            ("10-16T19:41:33", 6.7),
            ("10-05T15:52:50", 6.7),
            ("09-29T15:19:30", 7.0),
            ("09-11T00:20:52", 6.8),
            ("09-11T00:00:02", 6.6),
            ("09-10T13:08:14", 6.6),
            ("09-08T18:52:09", 6.9),
            ("08-25T13:22:01", 6.7),
            ("07-23T15:26:20", 6.8),
            ("07-19T09:27:04", 6.6),
            ("07-19T02:39:29", 6.9),
            ("07-05T02:12:06", 7.7),
            ("06-30T06:17:43", 7.0),
            ("06-27T11:40:15", 6.6),
            ("06-13T23:43:46", 6.9),
            ("06-01T14:31:01", 6.5),
            ("05-23T19:35:35", 6.5),
            ("05-12T06:27:59", 7.9),
            ("05-09T21:51:31", 6.8),
            ("05-07T16:45:21", 6.9),
            ("05-02T01:33:35", 6.6),
            ("04-24T12:14:50", 6.5),
            ("04-16T05:54:21", 6.6),
            ("04-15T22:59:54", 6.5),
            ("04-12T00:30:12", 7.1),
            ("04-09T12:46:12", 7.3),
            ("03-20T22:32:58", 7.1),
            ("03-03T14:11:15", 6.9),
            ("03-03T09:31:06", 6.5),
            ("02-25T21:02:19", 6.7),
            ("02-25T18:06:05", 6.6),
            ("02-25T08:36:33", 7.2),
            ("02-24T14:46:23", 6.5),
            ("02-23T15:57:19", 6.8),
            ("02-20T08:08:31", 7.3),
            ("02-14T12:08:57", 6.5),
            ("02-14T10:09:23", 6.9),
            ("02-12T12:50:19", 6.5),
            ("02-10T12:22:03", 6.5),
            ("02-08T09:38:13", 6.9),
            ("01-15T17:52:16", 6.5),
            ("01-05T11:01:05", 6.6)
        ],
        type_=ChartType.EFFECT_SCATTER)

# 在地图上绘制流向
geo.add("7级以上地震的时间连线",
        [   ("02-20T08:08:31","02-25T08:36:33"),
            ("02-25T08:36:33","03-20T22:32:58"),
            ("03-20T22:32:58","04-09T12:46:12"),
            ("04-09T12:46:12","04-12T00:30:12"),
            ("04-12T00:30:12","05-12T06:27:59"),
            ("05-12T06:27:59","06-30T06:17:43"),
            ("06-30T06:17:43","07-05T02:12:06"),
            ("07-05T02:12:06","09-29T15:19:30"),
            ("09-29T15:19:30","11-16T17:02:32"),
            ("11-16T17:02:32","11-24T09:03:00")
        ],
        type_= GeoType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5,color="black"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        color = "red"
       )


# 设置相关属性
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=6.5, max_=8),
                    title_opts=opts.TitleOpts(title="2008年全球发生的6.5级以上的地震"))

# 输出到网页文件
geo.render('./output/geo_earthquake.html')
