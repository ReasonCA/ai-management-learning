import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day5_review.csv")
df["销售额"] = df["销售额"].fillna(df["销售额" ].mean())

print("--- 填补缺失值后的完整数据 ---")
print(df)

grouped = df.groupby("大区")[["销售额","利润"]].sum()
print("\n--- 各大区销售额与利润汇总 ---")
print(grouped)

grouped_sorted = grouped.sort_values(by="销售额", ascending=False)
print("\n--- 按销售额降序排列 ---")
print(grouped_sorted)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

grouped_sorted.plot(kind="bar", y="销售额", title="各大区销售额对比")

plt.tight_layout()
plt.savefig("day5_sales_chart.png")
print("\n✅ 图表已保存为图片文件！")
