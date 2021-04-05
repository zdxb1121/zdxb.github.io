from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import WordCloud
from pyecharts.charts import Pie
from pyecharts.charts import Funnel

c = (
    Bar()
    .add_xaxis(["一到二十回","二十到四十回","四十到六十回","六十到八十回","八十到一百回","一百回到完结"])
    .add_yaxis("诸葛亮", [28,211,345,148,611,293])
    .add_yaxis("刘备", [224,330,305,160,18,2])
    .add_yaxis("曹操", [198,253,284,185,9,7])
    .add_yaxis("周瑜", [5,18,235,1,0,0])
    .set_global_opts(title_opts=opts.TitleOpts(title="三国人物出场"))
    .render("./output/bar_sanguo.html")
)
print("已生成人物出场统计图，按enter以继续...")

temp = input()

file_name = open('./data/人名.csv', 'r')
list_name = file_name.readlines()
file_name.close()

name = []  #用于保存元组(人物姓名,出现次数)
for line in list_name:
    line = line.strip()  #删除'\n'
    line_split = line.split(',')
    name.append((line_split[0],line_split[1]))

del name[0] #删除csv文件中的标题行

cloud = WordCloud()

cloud.add('', 
          name, #元组列表，词和词频
          shape='star', # 轮廓形状：'circle','cardioid','diamond',
                           # 'triangle-forward','triangle','pentagon','star'
          is_draw_out_of_bound = False, #允许词云超出画布边界
          word_size_range=[25, 50], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="华文行楷"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

cloud.set_global_opts(title_opts=opts.TitleOpts(title="三国人物词云"))

cloud.render('./output/wordcloud_sanguo_names.html')
print("已生成人物云图，按enter以继续...")

temp = input()

file_location = open('./data/地名.csv', 'r')
list_location = file_location.readlines()
file_location.close()

location = []  #用于保存元组(人物姓名,出现次数)
for line in list_location:
    line = line.strip()  #删除'\n'
    line_split = line.split(',')
    location.append((line_split[0],line_split[1]))

del location[0] #删除csv文件中的标题行

pie = Pie()
pie.add('', location[0:10])

pie.set_global_opts(title_opts=opts.TitleOpts(title = "三国地名饼图"))

pie.render('./output/wordcloud_sanguo_location.html')
print("已生成地名饼图，按enter以继续...")

temp = input()

file_weapon = open('./data/武器.csv', 'r')
list_weapon = file_weapon.readlines()
file_weapon.close()

weapon = []  #用于保存元组(人物姓名,出现次数)
for line in list_weapon:
    line = line.strip()  #删除'\n'
    line_split = line.split(',')
    weapon.append((line_split[0],line_split[1]))

del weapon[0] #删除csv文件中的标题行

funnel = Funnel()
funnel.add('', weapon)

funnel.set_global_opts(title_opts=opts.TitleOpts(title = "三国武器漏斗图"))

funnel.render('./output/wordcloud_sanguo_weapon.html')
print("已生成地名饼图，按enter以继续...")

temp = input()

