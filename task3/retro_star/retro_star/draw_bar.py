import matplotlib.pyplot as plt
import numpy as np

data1 = [17, 22, 26, 21, 23, 19, 16, 8, 9, 4, 4, 1, 9, 9, 2, 0]
data2 = [19, 17, 24, 20, 24, 14, 13, 9, 3, 2, 2, 6, 2, 2, 3, 2]
data3 = [17, 30, 23, 26, 20, 17, 16, 7, 10, 5, 6, 3, 0, 0, 0, 0]

# 创建x轴坐标
x = np.asarray(list(range(2,18)))


# 设置柱状图的宽度
width = 0.25

# 绘制柱状图
plt.bar(x - width, data1, width=width, label='Expert Route')
plt.bar(x, data2, width=width, label='Retro* Route')
plt.bar(x + width, data3, width=width, label='EG-MCTS Route')

# 添加标题和标签
# plt.title('Bar Chart')
plt.xlabel('Route Length')
plt.ylabel('Number')

# 设置x轴刻度标签
plt.xticks(x, x)

# 添加图例
plt.legend()

# 保存图像
plt.savefig('bar_chart.png')  # 保存为PNG格式，可以根据需要修改文件名和格式
