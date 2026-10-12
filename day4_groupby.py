import pandas as pd
import matplotlib.pyplot as plt
#读取数据
df = pd.read_csv("sales_data.csv")
#按“所属行业”分组，并计算“订单金额”和“员工人数”的总和
grouped = df.groupby("所属行业")[["订单金额","员工人数"]].sum()
print("--- 各行业订单金额与员工人数汇总 ---")
print(grouped)

# 3. 按“订单金额”从大到小排序
grouped_sorted = grouped.sort_values(by="订单金额",ascending=False)
print("\n--- 按订单金额降序排列 ---")
print(grouped_sorted)

# 4. 处理缺失值：用该列的平均值填补缺失的员工人数
df["员工人数"] = df["员工人数"].fillna(df["员工人数"].mean())

# 5. 画柱状图
# 解决中文显示问题（Windows系统）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

grouped_sorted.plot(kind="bar", y="订单金额",title="各行业订单金额对比")

# 6. 显示图表
plt.tight_layout()
plt.savefig("行业订单金额对比图.png") # 把图表保存为图片
