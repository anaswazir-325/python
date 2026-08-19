def currency(price , currency = "$"):
    return f"{price:.2f}{currency}"

print(currency(2))
print(currency(234, "pkr"))
    