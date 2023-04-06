from django import template

register=template.Library()

@register.filter(name="is_product_in_cart")
def is_product_in_cart(product , cart):
    print(product , cart)
    keys=cart.keys()                     
    for id in keys:
        if (product.id == int(id)) and (cart[id]>0):
            return True
    return False


@register.filter(name="product_quantity_in_cart")
def product_quantity_in_cart(product,cart):
    keys=cart.keys()                     
    for id in keys:
        if product.id == int(id):
            return cart[id]
    return 0



@register.filter(name='calculate_product_total_price')
def calculate_product_total_price(product,cart):
    return product.price * product_quantity_in_cart(product,cart)




@register.filter(name="tatal_price_of_item_in_cart")
def tatal_price_of_item_in_cart(products,cart):
    sum=0
    for product in products:
        sum+=calculate_product_total_price(product,cart)
    return sum