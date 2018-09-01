import matplotlib.pyplot as plt
from wordcloud import wordcloud
import jieba
filetext = open('shijiuda.txt',encoding='utf8').read()
wordlist = jieba.cut(filetext,cut_all = True)
wl_space_split = "".join(worldlist)
#设置词云属性，并生成词云
my_wordcloud = WordCloud(font_path= "C:\windowsFonts\simhei.ttf").generate(wl_space_split)
#以下三行绘图
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
