import pandas as pd
#读取csv文件
df = pd.read_csv("sales_data.csv")
#打印数据
print("--- 前3行数据 ---")
print(df.head(3))
print("\n--- 数据概况 ---")
df.info()
print("\n--- 描述性统计 ---")
print(df.describe())
print("\n--- 科技行业客户 ---")
tech_df = df[df["所属行业"] == "科技"]
print(tech_df)