from django import template


register = template.Library()
#Displays quantity of item
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity