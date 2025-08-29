import numpy as np
import matplotlib.pyplot as plt

# 创建参数t的数组
t = np.linspace(0, 2 * np.pi, 1000)

# 爱心曲线的参数方程
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# 创建图形和坐标轴，调整画布比例
fig, ax = plt.subplots(figsize=(10, 10))

# 绘制爱心，设置红色填充和黑色描边
ax.fill(x, y, color='red', edgecolor='black', linewidth=2)

# 调整坐标轴范围，确保爱心尖尖完全显示
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)  # 扩大y轴下限，显示爱心底部

# 隐藏坐标轴
ax.axis('off')

# 调整布局并显示图形
plt.tight_layout()
plt.show()
    