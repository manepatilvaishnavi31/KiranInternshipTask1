def calculateElectronicsGST(a, b):
    amount = a + b
    return amount + (amount * 18 / 100)


def calculateFashionGST(c, d):
    amount = c + d
    return amount + (amount * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100

    return total - discount


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics after GST: {:.2f}".format(electronics))
print("Fashion after GST: {:.2f}".format(fashion))
print("Food after GST: {:.2f}".format(food))
print("Total after GST: {:.2f}".format(total))
print("Discount: {:.2f}".format(total * 20 / 100))
print("Final payable amount: {:.2f}".format(final_amount))