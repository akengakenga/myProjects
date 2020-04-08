from urllib.parse import urlencode
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# x = np.random.randn(1,500)
# y = np.random.randn(1,500)
# # 使用反正切获取颜色，均匀分布在散点中（也可以不使用颜色）
# T=np.arctan2(x,y)
# ax = plt.subplot()
#
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('散点图')
# # c表示颜色,s表示散点的大小，alpha表示透明度，mark表示散点的形状
#
# plt.scatter(x,y,c=T,s=10,alpha = 0.8,marker='o')
# plt.grid(linestyle='-.')
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# plt.show()
# plt.bar()
path='1.txt'
text = open(path,encoding='utf-8').read()
wordcloud = WordCloud(background_color='white').generate(text)
plt.axis('off')
plt.imshow(wordcloud)
