import matplotlib.pyplot as plt

# 定义数据
x = [100, 200, 300, 400, 500]  # x轴数据
y_greedy_dfs = [38.42, 40.53, 44.21, 45.26, 46.84]  # Greedy DFS的y轴数据
y_retro_0 = [35.79, 58.42, 66.31, 72.63, 77.37]  # Retro*-0的y轴数据
y_retro = [51.58, 70.00, 76.32, 84.21, 86.84]  # Retro*的y轴数据
y_eg_mcts_0 = [57.24, 63.68, 68.42, 71.05, 73.68]  # EG-MCTS-0的y轴数据
y_eg_mcts = [90.00, 92.10, 94.21, 95.26, 96.84]  # EG-MCTS的y轴数据

# 设置颜色和标记样式
colors = ['blue', 'green', 'red', 'orange', 'purple']  # 颜色列表
markers = ['o', 's', 'D', 'v', 'p']  # 标记样式列表

# 绘制折线图
plt.plot(x, y_greedy_dfs, marker=markers[0], color=colors[0], label='Greedy DFS')
plt.plot(x, y_retro_0, marker=markers[0], color=colors[1], label='Retro*-0')
plt.plot(x, y_retro, marker=markers[0], color=colors[2], label='Retro*')
plt.plot(x, y_eg_mcts_0, marker=markers[0], color=colors[3], label='EG-MCTS-0')
plt.plot(x, y_eg_mcts, marker=markers[0], color=colors[4], label='EG-MCTS')

# 添加标题和标签
# plt.title("Success Rate vs. Iteration Limit")
plt.xlabel("Iteration Limit")
plt.ylabel("Success Rate (%)")

# 添加图例，将图例放置在整个图像的上方之外
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)

# 保存图像
plt.savefig('line_chart.png')  # 保存为PNG格式，可以根据需要修改文件名和格式

print("折线图已保存为line_chart.png")
