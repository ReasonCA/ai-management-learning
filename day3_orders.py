orders = [
    {"customer": "北京星辰科技", "amount": 25000},
    {"customer": "上海海联贸易", "amount": 8000},
    {"customer": "广州南方制造", "amount": 15000},
    {"customer": "深圳前海物流", "amount": 3000}
]
print("原始订单数据: ", orders)

def calculate_final_amount(amount):
    if amount >= 20000:
        discount_rate = 0.15
    elif amount >= 10000:
        discount_rate = 0.10
    elif amount >= 5000:
        discount_rate = 0.05
    else:
        discount_rate = 0.0
    final_amount = amount * (1 - discount_rate)
    return final_amount
print("25000元订单最终应付: ", calculate_final_amount(25000))
print("8000元订单最终应付: ",calculate_final_amount(8000))

print("\n--- 最终订单结算清单 ---")
for order in orders:
    customer_name = order["customer"]
    original_amount = order["amount"]
    final_amount = calculate_final_amount(original_amount)

    print(f"客户:{customer_name}")
    print(f"原价:{original_amount}元")
    print(f"最终应付:{final_amount:.2f}元")
    print("-"*30)