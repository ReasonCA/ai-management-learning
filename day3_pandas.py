import pandas as pd
#读取csv文件
#df:dataframe 数据框=虚拟的Excel表格
df = pd.read_csv("sales_data.csv")
#打印数据
print("--- 前3行数据 ---")
print(df.head(3))
print("\n--- 数据概况 ---")
df.info()
#info():告诉你这张表有几行、几列、每一列叫什么名字、每一列是不是数字类型（int, float）或者是文本类型（object）、有没有缺失值（Non-Null Count）。
print("\n--- 描述性统计 ---")
print(df.describe())
#describe() 是个超级实用的功能！它会自动帮你算出所有数字列的：数量(count)、平均值(mean)、标准差(std)、最小值(min)、最大值(max)、四分位数(25%, 50%, 75%)。
print("\n--- 科技行业客户 ---")
tech_df = df[df["所属行业"] == "科技"]
#tech_df = df[把行业是科技的行给我留下来]
print(tech_df)