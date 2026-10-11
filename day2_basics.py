employess = [
    {"name":"张三","score":92},
    {"name":"李四","score":78},
    {"name":"王五","score":65},
    {"name":"赵六","score":85}
]
print("员工名单:",employess)
print("第一位员工的名字是:",employess[0]["name"])

def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "合格"
    else:
        return "待改进"
print("92分是: ", get_grade(92))
print("78分是: ", get_grade(78))

print("\n--- 绩效评级结果 ---")
for emp in employess:
    name = emp["name"]
    score = emp["score"]
    grade = get_grade(score)
    print(f"{name}的分数是{score}, 评级为:{grade}")