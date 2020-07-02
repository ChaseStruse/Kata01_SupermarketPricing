# Want to make a 'Deals' function that will allow the user to indicate what deal is being run. 
from models import product
from models import deal

cannedBeans = product.Product()
cannedBeans.price = 2
cannedBeansDeal = deal.Deal()

print(cannedBeans.price)

#def createProductSale(cannedBeans, cannedBeansDeal):
