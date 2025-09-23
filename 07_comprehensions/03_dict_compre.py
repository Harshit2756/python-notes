tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Iced Lemon Tea": 60,
    "Iced Lemon Tea": 60,
    "Lemon Tea": 200
}

print(tea_prices_inr.items())
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)