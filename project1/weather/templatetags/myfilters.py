import datetime
from django import template    
register = template.Library()    

@register.filter('timestamp_to_time')
def convert_timestamp_to_time(timestamp):
    import time
    return (datetime.datetime.fromtimestamp(timestamp))
    # (datetime.datetime.fromtimestamp(1337453263.939))

# def ConvertFtoC(F):
    return (5 / 9) * (F - 32)
@register.filter('ftoc')
def convert_c(f):
 
    return (f-273.0)

