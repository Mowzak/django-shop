from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView,DetailView

from django.contrib.auth.decorators import user_passes_test


from app.models import *
from .filters import *
from .mixins import is_super
from django.urls import reverse_lazy
from django.db.models import Q




class home(is_super,ListView):
    # model = glasses
    context_object_name = 'glass'
    template_name = "modir/home.html"
    queryset = glasses.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        doc = {"شناسه":'id','عنوان':'title','قیمت':'price'}
        try:lst = glasses.objects.filter(Q(text__contains=request.POST['search'])|Q(title__contains=request.POST['search']))
        except:lst = glasses.objects.all()

        if request.POST['select']=='قیمت':
            lst =sorted(lst,key=lambda x:int((x.price).replace(",",""))) 
        else:
            lst = lst.order_by(doc[request.POST['select']])

        if 'radio1' in request.POST:
            lst = lst[::-1]
        return render(request,'modir/home.html',{'glass':lst}) 

    
class create(is_super,CreateView):
    model = glasses
    fields = ['title','bet','text','price','image','image2','image3']
    template_name = "modir/create.html"
    success_url = reverse_lazy("create")

@user_passes_test(lambda u: u.is_superuser,login_url='home')
def delete(r,pk):
    obj = get_object_or_404(glasses,pk=pk) 
    obj.delete()
    return redirect('modir')

class update(is_super,UpdateView):
    model = glasses
    template_name = "modir/update.html"
    fields = ['title','bet','text','price','image','image2','image3']
    # fields = ['post_save','user']
    success_url = reverse_lazy('modir')

@user_passes_test(lambda u: u.is_superuser,login_url='home')
def update_comment(r):

    for i in r.POST:
        try:
            obj = comment.objects.get(id=int(i))
            print(obj)
            print(obj.active)
            obj.active = not obj.active
            obj.save()
        except ValueError:
            pass
    return HttpResponseRedirect(r.META.get("HTTP_REFERER"))


class checkouts(is_super,ListView):
    context_object_name = 'checkobj'
    template_name = 'modir/checkouts.html'
    def get_queryset(self):
        qs = checkout.objects.all()
        return qs
    def post(self,r):
        query = checkout.objects.filter(Q(address__contains=r.POST['search'])|Q(postcode__contains=r.POST['search'])|Q(firstname__contains=r.POST['search'])|Q(lastname__contains=r.POST['search'])|Q(phone_number__contains=r.POST['search'])|Q(house_number__contains=r.POST['search'])|Q(price__contains=r.POST['search'])|Q(tracing__contains=r.POST['search']))

        if not r.POST['select']=='2':
            query = query.filter(valid=int(r.POST['select']))
        return render(r,'modir/checkouts.html',{'checkobj':query})


# def checkouts(r):
#     query = checkout.objects.all()
#     def post(self, r, *args, **kwargs):
#         print(r.POST)
#     return render(r,'modir/checkouts.html',{'checkobj':query})

class checkoutdet(is_super,DetailView):
    model = checkout
    context_object_name = 'checkobj'
    template_name = 'modir/updatecheck.html'
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(checkout,pk=int(request.POST['id']))
        obj.valid = not obj.valid
        obj.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@user_passes_test(lambda u: u.is_superuser,login_url='home')
def deletecheck(r,pk):
    obj = get_object_or_404(checkout,pk=pk) 
    obj.delete()
    return redirect('checkouts')

class aboutup(is_super,UpdateView):
    model = us
    fields = [
        'text',
        'text1',
        'text2',
        'text3',
        'image1',
        'image2',
        'image3',]
 
    template_name = 'modir/aboutus.html'
    success_url = reverse_lazy("aboutup",kwargs={'pk':'1'})

class homewidgets(is_super,ListView):
    model = homeview
    context_object_name = 'checkobj'
    template_name = 'modir/homewidgets.html'

class homewidget(is_super,CreateView):
    model = homeview
    fields = ['text','textb','image']
    template_name = "modir/homewidget.html"
    success_url = reverse_lazy("homewidget")
    
@user_passes_test(lambda u: u.is_superuser,login_url='home')
def deletewi(r,pk):
    obj = get_object_or_404(homeview,pk=pk) 
    obj.delete()
    return redirect('homewidgets')

class favpost(is_super,UpdateView):
    model = fav
    fields = [
        'fav',]
 
    template_name = 'modir/favpost.html'
    success_url = reverse_lazy("favpost",kwargs={'pk':'1'})