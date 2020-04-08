from django import template

register = template.Library()

@register.filter("strVal")
def strVal(value):
    return str(value)

@register.simple_tag
def mult2(v1,v2):
    return round(v1*v2,2)

@register.simple_tag
def mult3(v1,v2,v3):
    return round(v1*v2*v3,2)

@register.simple_tag
def selfadd(v1,v2):
    return round(v1+v2,2)