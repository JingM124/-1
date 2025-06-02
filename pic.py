import matplotlib
matplotlib.use('TkAgg')

import json
import matplotlib.pyplot as plt

with open('turning_trajectory_dataset.json', 'r') as f:
    data = json.load(f)

trajectory = data['trajectory']
x = [pt[0] for pt in trajectory]
y = [pt[1] for pt in trajectory]

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x, y, marker='o', markersize = 1, color ="white")
ax.scatter(x, y, s=3)  # 画点，点大小1

ax.set_title("Simulated Turning Trajectory")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

plt.savefig("trajectory.png", dpi=100)  # 保存为高分辨率 PNG 图像

plt.show()
