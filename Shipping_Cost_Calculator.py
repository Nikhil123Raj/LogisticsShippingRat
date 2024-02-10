# shipping cost calculator

## input package wight and shippingg rate
weight = float(input("enter the packaging weight in kilograms: "))
rate = float(input("enter the shipping rate perkilogram: "))

## calculate shipping cost
shipping_cost=weight*rate

##display the rate
print(f"shipping cost:{shipping_cost}USD")
