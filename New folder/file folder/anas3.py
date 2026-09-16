# with open ("Q1.txt","x") as file :
#     file.close()

# with open ("Q1.txt","r") as file :
#     count = 0 
#     for line in file: 
#         count += 1
# print(count)

# with open ("Q2.txt","w") as file:
#     for i in range(1,11):
#         file.write(str(i) + "\n")
# print("Number add")

# with open ("products.csv","x") as file :
#     file.close()
    
# import csv

# with open("products.csv", "r") as file:
#     reader = csv.DictReader(file)

#     expensive_product = None
#     highest_price = 0

#     for row in reader:
#         price = int(row["Price"])

#         if price > highest_price:
#             highest_price = price
#             expensive_product = row["Product"]

# print("Most expensive product:", expensive_product)
# print("Price:", highest_price)


