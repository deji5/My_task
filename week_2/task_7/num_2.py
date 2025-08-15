chewing_gum_price = float(input("enter price of chewing gum"))
rice_price = float(input("enter price of rice"))
ice_cream_price = float(input("ice cream price"))
price = {
    "chewing gum" : chewing_gum_price,
    "rice": rice_price,
    "ice cream" : ice_cream_price
}
print(f"chewing gum\t:\t{chewing_gum_price}\nrice\t:\t{rice_price}\nice cream\t:\t{ice_cream_price}")
price.update({"rice":7000})
print(price)
print(price.keys())