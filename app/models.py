from django.db import models
# import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.deletion import CASCADE
from django.utils.html import format_html
from django import forms
from django.core.validators import RegexValidator

hamedan_citys = [
    ('hmd','همدان'),
    ('mal','ملایر'),
    ('nah','نهاوند'),
    ('tos','تویسرکان'),
    ('kab','کبودرآهنگ'),
    ('asd','اسدآباد'),
    ('bah','بهار'),
    ('rzn','رزن'),
    ('dar','درگزین')
]
class Manager(models.Manager):
    def stor(self):
        print(self)
        return self
    


class glasses(models.Model):
    # ef=models.CharField(max_length=100, null=True, blank=True, unique=True)
    title = models.CharField(default="",max_length=50,verbose_name="موضوع")
    
    bet = models.TextField(default="",max_length=100,verbose_name="پیش نویس")
    # text = forms.CharField(label='text',س
    #                widget=forms.Tesxtarea(attrs={'class': 'ckeditor'}))
    text = RichTextUploadingField(verbose_name="متن")

    price = models.CharField(default="0",max_length=20,verbose_name="قیمت")
    image = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="عکس")
    image2 = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="")
    image3 = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="")


    def __str__(self):
        boom = f"{self.title} {self.price}"
        return boom
    
    def safe_text(self):
        safe = format_html(self.text)
        return safe
    
    # def get_absolute_url(self):
    #      return reverse('create')
    
    def img(self):
        return format_html(f"<img style='width:130px;height:100px;border-radius: 75px;border: 1px solid black; src='{self.image.url}'/>")
    class Meta:
        verbose_name = "عینک"
        verbose_name_plural = "عینک ها"

    objects = Manager()
class savee(models.Model):
    post_save = models.ManyToManyField(glasses,default=None,)
    # pro = models.IntegerField(unique=True,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    class Meta:
        verbose_name = "ذخیره"
        verbose_name_plural = "ذخیره شده ها"


#mozzz
class comment(models.Model):
    comment = models.TextField(default="",max_length=150,verbose_name='نظرات')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,verbose_name='کاربر')
    active = models.BooleanField(default=True,verbose_name='وضعیت')
    proid = models.ForeignKey(glasses,on_delete=CASCADE,verbose_name='محصول')

    def __str__(self):
        return f'{self.active}+{self.proid}'

    class Meta:
        ordering = ['active']
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

class like(models.Model):
    likee = models.ManyToManyField(User,default=None)
    post = models.ForeignKey(glasses,on_delete=CASCADE,default=None)
    def line_counter(self):
        return self.likee.count()
    
    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"

class us(models.Model):
    text = RichTextUploadingField(verbose_name="متن")
    text1 = RichTextUploadingField(verbose_name="متن")
    text2 = RichTextUploadingField(verbose_name="متن")
    text3 = RichTextUploadingField(verbose_name="متن")
    image1 = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="")
    image2 = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="")
    image3 = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="")

    class Meta:
        verbose_name = ""
        verbose_name_plural = "درباره ی ما"

    def __str__(self):
        return "فقط این"
class homeview(models.Model):
    text = models.CharField(default="",max_length=50,verbose_name="متن")
    textb = models.CharField(default="shop now",max_length=50,verbose_name="متن دکمه")
    image = models.ImageField(default='def.jpg',blank= True,upload_to="img/",verbose_name="عکس")

    def img(self):
        return format_html(f"<img style='width:110px;height:50px' src='{self.image.url}'/>")
    class Meta:
        verbose_name = ""
        verbose_name_plural = "متن ها در صفحه ی اصلی"


class fav(models.Model):
    fav = models.ManyToManyField(glasses,default=None)
    class Meta:
        verbose_name = ""
        verbose_name_plural = "پست های منتخب"

    def __str__(self):
        return "فقط این"

class checkout(models.Model):

    city = models.CharField(
        max_length=3,
        choices=hamedan_citys,
        default='hmd',
    )
    user = models.ForeignKey(User,on_delete=CASCADE,default=None)
    address = models.CharField(max_length=100,default="")
    postcode = models.CharField(max_length=10,default="",validators=[RegexValidator(r'[0-9]{10}', " کدپستی صحیح نیست ")])
    firstname = models.CharField(max_length=15,default="")
    lastname = models.CharField(max_length=15,default="")
    phone_number = models.CharField(max_length=15,default="",validators=[RegexValidator(r'[0-9]{10,11}', "تلفن همراه صحیح نیست ")])
    house_number = models.CharField(max_length=11,default="",validators=[RegexValidator(r'[0-9]{8,11}', "تلفن ثابت صحیح نیست ")])
    price = models.CharField(max_length=100,default="")
    valid = models.BooleanField(default=False)
    tracing = models.IntegerField(default=0)
    
    
