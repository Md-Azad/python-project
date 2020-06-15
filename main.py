import utility
#another way to import modules

from utility import multiply,divide  #( we can anso use * to import all modules at a  time)

import shopping.more_shopping.shopping_cart
# another way to import packages

from shopping.more_shopping import shopping_cart

print(utility.multiply(3,4))
print(utility.divide(4,2))


print(utility.multiply(5,10))
print(utility.divide(25,5))

print(shopping.more_shopping.shopping_cart.buy('apple'))

print(shopping_cart.buy('orange'))

if __name__== '__main__':
    print('please run this')


