#引入必要的函数库
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import sqlite3
import pandas as pd
#定义了一个将爬取到的视频数据添加到相应字典中的函数
def add_to_dict(lst, dic, l, n):
    if lst[0] in dic:
        if len(dic[lst[0]]) == (l + 1):
            pass
        elif len(dic[lst[0]]) == l:
            dic[lst[0]].append(lst[n])
    else:
        dic[lst[0]] = ["NA"]*l
        dic[lst[0]].append(lst[n])
        
video_play = {} #存储视频播放量的字典
video_like = {} #存储视频弹幕数量的字典
video_time = {"RunTime":[]} #存储单次爬取运行时间的字典，之所以不用列表是因为字典类型方便后续操作
time_list = [] #存储时间戳的列表，记录的是爬取完毕时的时间
num = 10 #每爬取到10条数据就存入数据库，防止因为设备问题导致过多数据丢失
times = 1000 #总共爬取100次也就是1000条数据时结束一张表的存储
#单张表数据爬取以及存储的循环嵌套
for i in range(times):
    for j in range(num):
        start = time.time() #记录下开始时间，从尝试打开网页开始
        #利用试错机制规避由于网络波动导致的页面加载失败，防止程序报错终止运行
        try:
            #打开网页
            options = Options()
            options.add_argument("--headless") 
            browser = webdriver.Chrome(options=options)
            browser.get('https://www.bilibili.com/v/popular/all') #这是b站的热门视频页面，无需登录即可进入
            wait = WebDriverWait(browser, 60)
            #获取网页资源，并将热门视频的前20条数据爬取下来
            pq_doc = pq(browser.page_source)
            for k in range(1,21):
                item = pq_doc('#app > div.popular-video-container.popular-list > div.flow-loader > ul.card-list > div:nth-child({})'.format(k))
                #按照["视频的名称以及作者","播放量","弹幕数"]的顺序，将视频信息存储进一个列表中
                video = [item.find('div.video-card__info > p').text().replace("\'", "‘") + "_by_"+item.find('div.video-card__info > div > span.up-name > span').text(), item.find('div.video-card__info > div > p > span.play-text').text(), item.find('div.video-card__info > div > p > span.like-text').text()]
                #将视频信息对应地暂存进字典中
                add_to_dict(video, video_play, i*num + j, 1)
                add_to_dict(video, video_like, i*num + j, 2)
            #结束单次的爬取
            browser.close()
        except:
            #如果出了问题，就报错
            print("出了点问题！",end = " ")
        #将运行结束的时间记录下来，存储到时间戳列表中
        time_list.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #由于存在页面加载不全以及热门视频流动变化等问题，每次爬取后都将数据量补齐，使之能与时间戳数量对应，防止在转存df的时候
        for key in video_play.keys():
            length = len(video_play[key])
            video_play[key] += ["NA"]*(len(time_list) - length)
            length = len(video_like[key])
            video_like[key] += ["NA"]*(len(time_list) - length)
        end = time.time()
        print("第{}次爬取已经结束".format(i*num + j + 1) + ",用时{}秒".format(int(end-start)))
        #将程序的运行时间保存下来
        video_time["RunTime"].append(int(end-start))
    #由于之前测试的时候这一部分出现了我没能解决的问题，因此在这里添加了试错机制
    try:
        #将数据存储成df的形式
        df_play = pd.DataFrame(video_play, index=time_list) 
        df_like = pd.DataFrame(video_like, index=time_list)
        df_time = pd.DataFrame(video_time, index=time_list)
        #连接数据库，直接将df的数据转存到sql中
        conn = sqlite3.connect('../other/bilibili.db')
        pd.io.sql.to_sql(df_play, "play", con = conn, if_exists = "replace")
        pd.io.sql.to_sql(df_like, "like", con = conn, if_exists = "replace")
        pd.io.sql.to_sql(df_time, "run" , con = conn, if_exists = "replace")
        conn.close()
        print("\n共{}轮数据已经处理完成!\n".format(i + 1))
    #如果报错则跳过本次存储
    except:
        pass