from django.contrib import admin

# Register your models here.
from . import models

class glos(admin.ModelAdmin):
    list_display = ('title','bet','safe_text','price','img')
    list_filter = ("title",'id')
    search_fields =("title",'bet','price','id')
admin.site.register(models.glasses,glos)
######################################
# @admin.action(description='غیر فعال کردن کامنت ها')
def make_f(modeladmin, request, queryset):
    queryset.update(active=False)

# @admin.action(description='فعال کردن کامنت ها')
def make_t(modeladmin, request, queryset):
    queryset.update(active=True)

class comment_check(admin.ModelAdmin):
    list_display = ('comment','user','active','proid')
    list_filter = ("active",'user','proid')
    search_fields = ("comment",)
    actions = [make_f,make_t]
admin.site.register(models.comment,comment_check)

admin.site.register(models.like)
admin.site.register(models.savee)
admin.site.register(models.us)
class view_admin(admin.ModelAdmin):
    list_display = ('text','textb','img')
admin.site.register(models.homeview,view_admin)
admin.site.register(models.fav)
admin.site.register(models.checkout)

