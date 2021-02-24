## 2. Calculate the Profit
## You work for a manufacturer, and have been asked to calculate the total profit
## made on the sales of a product. You are given a dictionary containing the cost
## price per unit (in dollars), sell price per unit (in dollars), and the starting
## inventory. Return the total profit made, rounded to the nearest dollar. Assume
## all of the inventory has been sold.
## Examples
## profit({
##  "cost_price": 32.67,
##  "sell_price": 45.00,
##  "inventory": 1200
## }) ➞ 14796
##
## profit({
##  "cost_price": 225.89,
##  "sell_price": 550.00,
##  "inventory": 100
## }) ➞ 32411
##
## profit({
##  "cost_price": 2.77,
##  "sell_price": 7.95,
##  "inventory": 8500
## }) ➞ 44030
## Notes
## Profit = Total Sales - Total Cost

def count_profit (cost_price, sell_price, inventory):
    return int(sell_price * inventory - cost_price * inventory)
    

cost_price = int (input ("Input cost price "))
sell_price = int (input ("Input sell price "))
inventory = int (input ("Input inventory "))
print ("Profit = %d" %count_profit (cost_price, sell_price, inventory))
