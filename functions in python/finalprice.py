def finalprice(price,discount=5):
    finalprice=price-(price*(discount/100))
    print("The finalprice is",finalprice)
finalprice(1000)