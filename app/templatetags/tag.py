from django import template
from django.db import models
from ..models import checkout, us,comment,like,glasses,savee
from django.utils.html import strip_tags
register = template.Library()
@register.filter(name='liked')
def liked(v):
    like_obg = like.objects.get_or_create(post=glasses.objects.get(id=int(v)))
    return like_obg[0].line_counter()

@register.filter(name='shoped')
def shoped(v):
    try:lst = savee.objects.get(user=v).post_save.all()
    except:lst = []
    return len(lst)
@register.filter(name='shoped_p')
def shoped_p(v):
    try:lst = savee.objects.get(user=v).post_save.all()
    except:lst = []
    return lst

@register.filter(name='ustem')
def ustem(v):
    obj = (strip_tags(us.objects.get(id=1).text)).replace('&zwnj;','‌‌‌‌‌‌ ')
    return obj

    
@register.filter(name='saves')
def savecollecter(pk):
    pk = int(pk.split("/")[-1])
    obj = savee.objects.filter(post_save__id=pk)
    return obj
    
@register.filter(name='likes')
def likecollecter(pk):
    pk = int(pk.split("/")[-1])
    try:
        obj = like.objects.get(post__id=pk)
    except:
        return None
        
    return [i.username for i in obj.likee.all()]

@register.filter(name='comment')
def commentUP(pk):
    pk = int(pk.split("/")[-1])
    obj = comment.objects.filter(proid__pk=pk)
    return obj

@register.filter(name='addclass')
def addclass(string,clas):
    string = string.replace("<p>",f'<p class="{clas}">')
    return string

@register.filter(name='total')
def total_price(user):
    lst = savee.objects.get_or_create(user=user)[0].post_save.all()
    

    counter = 0
    for i in lst:
        try:
            counter+=int(i.price.replace(",",""))
        except ValueError:
            t = glasses.objects.filter(price=i.price)
            t.delete()
    return counter

@register.filter(name='check_count')
def check_count(a):
    return checkout.objects.filter(valid=False).count()

@register.filter(name='checkoutpreview')
def checkoutpreview(a):

    val = checkout.objects.filter(valid=False)[:3]
    print(val)
    return val