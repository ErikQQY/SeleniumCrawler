import time
from selenium import webdriver
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

#设定专辑内容，初始化歌曲提及频率
songs=["beautiful people","remember the name","put it all on me","antisocial","blow","way to break my heart","feels","nothing on you","best part of me","i don't care","south of the border","cross me","1000 nights","take me back to london","i don't want your money"]
songs_frequency=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count1=0 #是否写入评论数
count2=0 #记录当前写入评论数
count3=0 #每循环10次输出一次时间

#提前为selenium中要用到的JavaScript代码初始化值
now_height=0
pre_height=0

#创建浏览器驱动
wd=webdriver.Chrome()
url="https://www.youtube.com/post/UgxSXlrxP5BQG0l5IZR4AaABCQ?lc=UgzSGOkB7gRj7WVdJ5R4AaABAg"
wd.get(url)

#YouTube上Selenium先滚动页面后提取内容
while True:
    try:
        #不断拖拉滚动条
        wd.execute_script("scrollBy(0,100000)")
        time.sleep(1)
        if count3%20==0:
            print("count:"+str(count3))
            now_height=wd.execute_script("return document.documentElement.scrollHeight;")
            if now_height==pre_height:
                break
            pre_height=now_height
        count3+=1
    except Exception as e:
        print(e)

#Selenium查找内容
comment=wd.find_elements_by_id("content-text")
comments=[com.text for com in comment]

for m in range(len(songs)):
    for i in range(len(comments)):
        if comments[i].lower().find(songs[m])!=-1:
            songs_frequency[m]+=1
            
#单纯为了美观~~~
songs_capital=[m.capitalize() for m in songs]

#形成字典
songs_frequency_dict=dict(zip(songs_capital,songs_frequency))

#画词云函数
def draw_cloud(dic):
    image=Image.open('project.jpg')

    wc=WordCloud(scale=4,font_path='simkai.ttf',background_color='white',max_font_size=60)
    wc.generate_from_frequencies(dic)
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig("NO6.jpg",dpi=my_dpi)
    plt.show()
    

draw_cloud(songs_frequency_dict)