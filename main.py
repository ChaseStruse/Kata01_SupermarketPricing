from deal import Deal
from product import Product

beanName = "Canned Beans"
beanCost = 2
beanQuantity = 10
beansOnSale = True

buyThreeGetOneFreeDealOnBeans = Deal()
cannedBeans = Product(beanName, beanCost, beanQuantity, beansOnSale)
buyThreeGetOneFreeDealOnBeans.dealPrice = cannedBeans.price * 3
buyThreeGetOneFreeDealOnBeans.maxQuantity = 4
cannedBeans.deal = buyThreeGetOneFreeDealOnBeans

def calculateCostAfterDeal(item):
  if(item.quantity <= item.deal.maxQuantity):
    return(item.deal.dealPrice * item.quantity)
  else:
    totalCostForItemsThatQualifyForDeal = item.deal.dealPrice * item.deal.maxQuantity
    totalCostForItemsThatDoNotQualifyForDeal = item.price * (item.quantity - item.deal.maxQuantity)
    total = totalCostForItemsThatDoNotQualifyForDeal + totalCostForItemsThatQualifyForDeal
    print("Total dont qualify= ", totalCostForItemsThatDoNotQualifyForDeal)
    print("Total do qualify= ", totalCostForItemsThatQualifyForDeal)
    return(total)

def calculateCost(item):
  if(item.onSale):
    return(calculateCostAfterDeal(item))
  else:
    return(item.price * item.quantity)

def checkout(items):
  for item in items:
    return(calculateCost(item));
    
def main():
  print(cannedBeans.deal.dealPrice)
  items = [cannedBeans]
  print("Total cost = ", checkout(items))

main()