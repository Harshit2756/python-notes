users  = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]

discounts = {
    "P20":(0.2, 0),
    "F10":(0, 10),
    "P50":(0.5, 0)
}

# so to access the discounts dictionary, we need to get the coupon code from each user

for user in users:
    # percent , fixed = discounts[user["coupon"]]
    percent , fixed = discounts.get(user["coupon"], (0, 0))  # default to no discount if coupon not found  
    discount = user["total"] * percent + fixed
    total = user["total"] - discount
    print(f"User total after discount: {total}")
